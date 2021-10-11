## GOlang GC
#### 三色标记法
1. 三色
  - 白色对象，潜在的垃圾，其内存可能会被垃圾收集器回收
  - 灰色对象，引用了其他对象
  - 黑色对象，活跃的对象

2. 原理
  - 把所有对象放到白色集合中
  - root set遍历，遍历到的白色对象放到灰色中
  - 遍历灰色对象，把灰色对象引用到的白色对象放到灰色集合中
  - 循环上一步骤，灰色中没有就终止
  - 白色集合中的对象就是不可达对象，进行垃圾回收

#### 写屏障（write barrier）
1. GC时是不会STW（stop the world），此时对象还可以修改
2. 混合写屏障会同时标记指针写入目标的"原指针"和“新指针".使得其不会被回收
3. GC过程中，所有新分配对象会被标记为黑色
  
#### 辅助GC
1. 速度跟不上用户分配速度时，暂停用户线程/协程，叫做辅助GC


#### 源码
1. gc开始入口
```
// gcStart starts the GC. It transitions from _GCoff to _GCmark (if
// debug.gcstoptheworld == 0) or performs all of GC (if
// debug.gcstoptheworld != 0).
//
// This may return without performing this transition in some cases,
// such as when called on a system stack or with locks held.
func gcStart(trigger gcTrigger) {
	// Since this is called from malloc and malloc is called in
	// the guts of a number of libraries that might be holding
	// locks, don't attempt to start GC in non-preemptible or
	// potentially unstable situations.
	mp := acquirem()
	if gp := getg(); gp == mp.g0 || mp.locks > 1 || mp.preemptoff != "" {
		releasem(mp)
		return
	}
	releasem(mp)
	mp = nil

	// Pick up the remaining unswept/not being swept spans concurrently
	//
	// This shouldn't happen if we're being invoked in background
	// mode since proportional sweep should have just finished
	// sweeping everything, but rounding errors, etc, may leave a
	// few spans unswept. In forced mode, this is necessary since
	// GC can be forced at any point in the sweeping cycle.
	//
	// We check the transition condition continuously here in case
	// this G gets delayed in to the next GC cycle.
	for trigger.test() && sweepone() != ^uintptr(0) {
		sweep.nbgsweep++
	}

	// Perform GC initialization and the sweep termination
	// transition.
	semacquire(&work.startSema)
	// Re-check transition condition under transition lock.
	if !trigger.test() {
		semrelease(&work.startSema)
		return
	}

	// For stats, check if this GC was forced by the user.
	work.userForced = trigger.kind == gcTriggerAlways || trigger.kind == gcTriggerCycle

	// In gcstoptheworld debug mode, upgrade the mode accordingly.
	// We do this after re-checking the transition condition so
	// that multiple goroutines that detect the heap trigger don't
	// start multiple STW GCs.
	mode := gcBackgroundMode
	if debug.gcstoptheworld == 1 {
		mode = gcForceMode
	} else if debug.gcstoptheworld == 2 {
		mode = gcForceBlockMode
	}

	// Ok, we're doing it! Stop everybody else
	semacquire(&worldsema)

	if trace.enabled {
		traceGCStart()
	}

	// Check that all Ps have finished deferred mcache flushes.
	for _, p := range allp {
		if fg := atomic.Load(&p.mcache.flushGen); fg != mheap_.sweepgen {
			println("runtime: p", p.id, "flushGen", fg, "!= sweepgen", mheap_.sweepgen)
			throw("p mcache not flushed")
		}
	}

	gcBgMarkStartWorkers() // 标记入口

	gcResetMarkState()

	work.stwprocs, work.maxprocs = gomaxprocs, gomaxprocs
	if work.stwprocs > ncpu {
		// This is used to compute CPU time of the STW phases,
		// so it can't be more than ncpu, even if GOMAXPROCS is.
		work.stwprocs = ncpu
	}
	work.heap0 = atomic.Load64(&memstats.heap_live)
	work.pauseNS = 0
	work.mode = mode

	now := nanotime()
	work.tSweepTerm = now
	work.pauseStart = now
	if trace.enabled {
		traceGCSTWStart(1)
	}
	systemstack(stopTheWorldWithSema)
	// Finish sweep before we start concurrent scan.
	systemstack(func() {
		finishsweep_m()
	})
	// clearpools before we start the GC. If we wait they memory will not be
	// reclaimed until the next GC cycle.
	clearpools()

	work.cycles++

	gcController.startCycle()
	work.heapGoal = memstats.next_gc

	// In STW mode, disable scheduling of user Gs. This may also
	// disable scheduling of this goroutine, so it may block as
	// soon as we start the world again.
	if mode != gcBackgroundMode {
		schedEnableUser(false)
	}

	// Enter concurrent mark phase and enable
	// write barriers.
	//
	// Because the world is stopped, all Ps will
	// observe that write barriers are enabled by
	// the time we start the world and begin
	// scanning.
	//
	// Write barriers must be enabled before assists are
	// enabled because they must be enabled before
	// any non-leaf heap objects are marked. Since
	// allocations are blocked until assists can
	// happen, we want enable assists as early as
	// possible.
	setGCPhase(_GCmark)  // 设置gc的状态为_GCmark

	gcBgMarkPrepare() // Must happen before assist enable.
	gcMarkRootPrepare()

	// Mark all active tinyalloc blocks. Since we're
	// allocating from these, they need to be black like
	// other allocations. The alternative is to blacken
	// the tiny block on every allocation from it, which
	// would slow down the tiny allocator.
	gcMarkTinyAllocs()

	// At this point all Ps have enabled the write
	// barrier, thus maintaining the no white to
	// black invariant. Enable mutator assists to
	// put back-pressure on fast allocating
	// mutators.
	atomic.Store(&gcBlackenEnabled, 1)

	// Assists and workers can start the moment we start
	// the world.
	gcController.markStartTime = now

	// Concurrent mark.
	systemstack(func() {
		now = startTheWorldWithSema(trace.enabled)
		work.pauseNS += now - work.pauseStart
		work.tMark = now
	})
	// In STW mode, we could block the instant systemstack
	// returns, so don't do anything important here. Make sure we
	// block rather than returning to user code.
	if mode != gcBackgroundMode {
		Gosched()
	}

	semrelease(&work.startSema)
}
```
2. 标记准备
```
func gcBgMarkStartWorkers() {
	// Background marking is performed by per-P G's. Ensure that
	// each P has a background GC G.
	for _, p := range allp {
		if p.gcBgMarkWorker == 0 {
			go gcBgMarkWorker(p)
			notetsleepg(&work.bgMarkReady, -1)  // 睡眠，因为此时，gc的状态并未为gcmark，setGCPhase(_GCmark)该调用设置gc状态
			noteclear(&work.bgMarkReady)
		}
	}
}
```
3. 三色标记实现
```
func gcDrain(gcw *gcWork, flags gcDrainFlags) {
    // ...一些准备+判断
  
    // Drain root marking jobs.
    if work.markrootNext < work.markrootJobs {
        for !(preemptible && gp.preempt) {
            job := atomic.Xadd(&work.markrootNext, +1) - 1
            if job >= work.markrootJobs {
                break
            }
            // 扫描root set
            markroot(gcw, job)
            if check != nil && check() {
                goto done
            }
        }
    }

    // Drain heap marking jobs.
    // 循环直到被抢占
    for !(preemptible && gp.preempt) {
        // Try to keep work available on the global queue. We used to
        // check if there were waiting workers, but it's better to
        // just keep work available than to make workers wait. In the
        // worst case, we'll do O(log(_WorkbufSize)) unnecessary
        // balances.
        if work.full == 0 {
            gcw.balance()
        }

        var b uintptr
        if blocking {
            b = gcw.get()
        } else {
            b = gcw.tryGetFast()
            if b == 0 {
                b = gcw.tryGet()
            }
        }
        if b == 0 {
            // work barrier reached or tryGet failed.
            break
        }
        // 扫描获取的到对象
        scanobject(b, gcw)

        // Flush background scan work credit to the global
        // account if we've accumulated enough locally so
        // mutator assists can draw on it.
        if gcw.scanWork >= gcCreditSlack {
            atomic.Xaddint64(&gcController.scanWork, gcw.scanWork)
            if flushBgCredit {
                gcFlushBgCredit(gcw.scanWork - initScanWork)
                initScanWork = 0
            }
            checkWork -= gcw.scanWork
            gcw.scanWork = 0
            if checkWork <= 0 {
                checkWork += drainCheckThreshold
                if check != nil && check() {
                    break
                }
            }
        }
    }

    // In blocking mode, write barriers are not allowed after this
    // point because we must preserve the condition that the work
    // buffers are empty.

done:
    // Flush remaining scan work credit.
    if gcw.scanWork > 0 {
        // 把扫描的对象数量添加到全局
        atomic.Xaddint64(&gcController.scanWork, gcw.scanWork)
        if flushBgCredit {
            gcFlushBgCredit(gcw.scanWork - initScanWork)
        }
        gcw.scanWork = 0
    }
}
```

4. root set 扫描
```
// markroot scans the i'th root.
//
// Preemption must be disabled (because this uses a gcWork).
//
// nowritebarrier is only advisory here.
//
//go:nowritebarrier
func markroot(gcw *gcWork, i uint32) {
	// TODO(austin): This is a bit ridiculous. Compute and store
	// the bases in gcMarkRootPrepare instead of the counts.
	baseFlushCache := uint32(fixedRootCount)
	baseData := baseFlushCache + uint32(work.nFlushCacheRoots)
	baseBSS := baseData + uint32(work.nDataRoots)
	baseSpans := baseBSS + uint32(work.nBSSRoots)
	baseStacks := baseSpans + uint32(work.nSpanRoots)
	end := baseStacks + uint32(work.nStackRoots)

	// Note: if you add a case here, please also update heapdump.go:dumproots.
	switch {
	case baseFlushCache <= i && i < baseData:
		flushmcache(int(i - baseFlushCache))

	case baseData <= i && i < baseBSS:
		for _, datap := range activeModules() {
			markrootBlock(datap.data, datap.edata-datap.data, datap.gcdatamask.bytedata, gcw, int(i-baseData))
		}

	case baseBSS <= i && i < baseSpans:
		for _, datap := range activeModules() {
			markrootBlock(datap.bss, datap.ebss-datap.bss, datap.gcbssmask.bytedata, gcw, int(i-baseBSS))
		}

	case i == fixedRootFinalizers:
		for fb := allfin; fb != nil; fb = fb.alllink {
			cnt := uintptr(atomic.Load(&fb.cnt))
			scanblock(uintptr(unsafe.Pointer(&fb.fin[0])), cnt*unsafe.Sizeof(fb.fin[0]), &finptrmask[0], gcw, nil)
		}

	case i == fixedRootFreeGStacks:
		// Switch to the system stack so we can call
		// stackfree.
		systemstack(markrootFreeGStacks)

	case baseSpans <= i && i < baseStacks:
		// mark mspan.specials
		markrootSpans(gcw, int(i-baseSpans))

	default:
		// the rest is scanning goroutine stacks
		var gp *g
		if baseStacks <= i && i < end {
			gp = allgs[i-baseStacks]
		} else {
			throw("markroot: bad index")
		}

		// remember when we've first observed the G blocked
		// needed only to output in traceback
		status := readgstatus(gp) // We are not in a scan state
		if (status == _Gwaiting || status == _Gsyscall) && gp.waitsince == 0 {
			gp.waitsince = work.tstart
		}

		// scang must be done on the system stack in case
		// we're trying to scan our own stack.
		systemstack(func() {
			// If this is a self-scan, put the user G in
			// _Gwaiting to prevent self-deadlock. It may
			// already be in _Gwaiting if this is a mark
			// worker or we're in mark termination.
			userG := getg().m.curg
			selfScan := gp == userG && readgstatus(userG) == _Grunning
			if selfScan {
				casgstatus(userG, _Grunning, _Gwaiting)
				userG.waitreason = waitReasonGarbageCollectionScan
			}

			// TODO: scang blocks until gp's stack has
			// been scanned, which may take a while for
			// running goroutines. Consider doing this in
			// two phases where the first is non-blocking:
			// we scan the stacks we can and ask running
			// goroutines to scan themselves; and the
			// second blocks.
			scang(gp, gcw)

			if selfScan {
				casgstatus(userG, _Gwaiting, _Grunning)
			}
		})
	}
}
```

5. 扫描结束,关闭写屏障等
```
func gcMarkTermination(nextTriggerRatio float64) {
	// World is stopped.
	// Start marktermination which includes enabling the write barrier.
	atomic.Store(&gcBlackenEnabled, 0)
	setGCPhase(_GCmarktermination)

	work.heap1 = memstats.heap_live
	startTime := nanotime()

	mp := acquirem()
	mp.preemptoff = "gcing"
	_g_ := getg()
	_g_.m.traceback = 2
	gp := _g_.m.curg
	casgstatus(gp, _Grunning, _Gwaiting)
	gp.waitreason = waitReasonGarbageCollection

	// Run gc on the g0 stack. We do this so that the g stack
	// we're currently running on will no longer change. Cuts
	// the root set down a bit (g0 stacks are not scanned, and
	// we don't need to scan gc's internal state).  We also
	// need to switch to g0 so we can shrink the stack.
	systemstack(func() {
		gcMark(startTime)
		// Must return immediately.
		// The outer function's stack may have moved
		// during gcMark (it shrinks stacks, including the
		// outer function's stack), so we must not refer
		// to any of its variables. Return back to the
		// non-system stack to pick up the new addresses
		// before continuing.
	})

	systemstack(func() {
		work.heap2 = work.bytesMarked
		if debug.gccheckmark > 0 {
			// Run a full non-parallel, stop-the-world
			// mark using checkmark bits, to check that we
			// didn't forget to mark anything during the
			// concurrent mark process.
			gcResetMarkState()
			initCheckmarks()
			gcw := &getg().m.p.ptr().gcw
			gcDrain(gcw, 0)
			wbBufFlush1(getg().m.p.ptr())
			gcw.dispose()
			clearCheckmarks()
		}

		// marking is complete so we can turn the write barrier off
		setGCPhase(_GCoff)
		gcSweep(work.mode)
	})

	_g_.m.traceback = 0
	casgstatus(gp, _Gwaiting, _Grunning)

	if trace.enabled {
		traceGCDone()
	}

	// all done
	mp.preemptoff = ""

	if gcphase != _GCoff {
		throw("gc done but gcphase != _GCoff")
	}

	// Update GC trigger and pacing for the next cycle.
	gcSetTriggerRatio(nextTriggerRatio)

	// Update timing memstats
	now := nanotime()
	sec, nsec, _ := time_now()
	unixNow := sec*1e9 + int64(nsec)
	work.pauseNS += now - work.pauseStart
	work.tEnd = now
	atomic.Store64(&memstats.last_gc_unix, uint64(unixNow)) // must be Unix time to make sense to user
	atomic.Store64(&memstats.last_gc_nanotime, uint64(now)) // monotonic time for us
	memstats.pause_ns[memstats.numgc%uint32(len(memstats.pause_ns))] = uint64(work.pauseNS)
	memstats.pause_end[memstats.numgc%uint32(len(memstats.pause_end))] = uint64(unixNow)
	memstats.pause_total_ns += uint64(work.pauseNS)

	// Update work.totaltime.
	sweepTermCpu := int64(work.stwprocs) * (work.tMark - work.tSweepTerm)
	// We report idle marking time below, but omit it from the
	// overall utilization here since it's "free".
	markCpu := gcController.assistTime + gcController.dedicatedMarkTime + gcController.fractionalMarkTime
	markTermCpu := int64(work.stwprocs) * (work.tEnd - work.tMarkTerm)
	cycleCpu := sweepTermCpu + markCpu + markTermCpu
	work.totaltime += cycleCpu

	// Compute overall GC CPU utilization.
	totalCpu := sched.totaltime + (now-sched.procresizetime)*int64(gomaxprocs)
	memstats.gc_cpu_fraction = float64(work.totaltime) / float64(totalCpu)

	// Reset sweep state.
	sweep.nbgsweep = 0
	sweep.npausesweep = 0

	if work.userForced {
		memstats.numforcedgc++
	}

	// Bump GC cycle count and wake goroutines waiting on sweep.
	lock(&work.sweepWaiters.lock)
	memstats.numgc++
	injectglist(&work.sweepWaiters.list)
	unlock(&work.sweepWaiters.lock)

	// Finish the current heap profiling cycle and start a new
	// heap profiling cycle. We do this before starting the world
	// so events don't leak into the wrong cycle.
	mProf_NextCycle()

	systemstack(func() { startTheWorldWithSema(true) })

	// Flush the heap profile so we can start a new cycle next GC.
	// This is relatively expensive, so we don't do it with the
	// world stopped.
	mProf_Flush()

	// Prepare workbufs for freeing by the sweeper. We do this
	// asynchronously because it can take non-trivial time.
	prepareFreeWorkbufs()

	// Free stack spans. This must be done between GC cycles.
	systemstack(freeStackSpans)

	// Ensure all mcaches are flushed. Each P will flush its own
	// mcache before allocating, but idle Ps may not. Since this
	// is necessary to sweep all spans, we need to ensure all
	// mcaches are flushed before we start the next GC cycle.
	systemstack(func() {
		forEachP(func(_p_ *p) {
			_p_.mcache.prepareForSweep()
		})
	})

	// Print gctrace before dropping worldsema. As soon as we drop
	// worldsema another cycle could start and smash the stats
	// we're trying to print.
	if debug.gctrace > 0 {
		util := int(memstats.gc_cpu_fraction * 100)

		var sbuf [24]byte
		printlock()
		print("gc ", memstats.numgc,
			" @", string(itoaDiv(sbuf[:], uint64(work.tSweepTerm-runtimeInitTime)/1e6, 3)), "s ",
			util, "%: ")
		prev := work.tSweepTerm
		for i, ns := range []int64{work.tMark, work.tMarkTerm, work.tEnd} {
			if i != 0 {
				print("+")
			}
			print(string(fmtNSAsMS(sbuf[:], uint64(ns-prev))))
			prev = ns
		}
		print(" ms clock, ")
		for i, ns := range []int64{sweepTermCpu, gcController.assistTime, gcController.dedicatedMarkTime + gcController.fractionalMarkTime, gcController.idleMarkTime, markTermCpu} {
			if i == 2 || i == 3 {
				// Separate mark time components with /.
				print("/")
			} else if i != 0 {
				print("+")
			}
			print(string(fmtNSAsMS(sbuf[:], uint64(ns))))
		}
		print(" ms cpu, ",
			work.heap0>>20, "->", work.heap1>>20, "->", work.heap2>>20, " MB, ",
			work.heapGoal>>20, " MB goal, ",
			work.maxprocs, " P")
		if work.userForced {
			print(" (forced)")
		}
		print("\n")
		printunlock()
	}

	semrelease(&worldsema)
	// Careful: another GC cycle may start now.

	releasem(mp)
	mp = nil

	// now that gc is done, kick off finalizer thread if needed
	if !concurrentSweep {
		// give the queued finalizers, if any, a chance to run
		Gosched()
	}
}
```

6. GCmark
```
func setGCPhase(x uint32) {
	atomic.Store(&gcphase, x)
	writeBarrier.needed = gcphase == _GCmark || gcphase == _GCmarktermination
	writeBarrier.enabled = writeBarrier.needed || writeBarrier.cgo
}
```
7. gcSweep
```
func gcSweep(mode gcMode) {
	if gcphase != _GCoff {
		throw("gcSweep being done but phase is not GCoff")
	}

	lock(&mheap_.lock)
	mheap_.sweepgen += 2
	mheap_.sweepdone = 0
	if mheap_.sweepSpans[mheap_.sweepgen/2%2].index != 0 {
		// We should have drained this list during the last
		// sweep phase. We certainly need to start this phase
		// with an empty swept list.
		throw("non-empty swept list")
	}
	mheap_.pagesSwept = 0
	mheap_.sweepArenas = mheap_.allArenas
	mheap_.reclaimIndex = 0
	mheap_.reclaimCredit = 0
	unlock(&mheap_.lock)

	if !_ConcurrentSweep || mode == gcForceBlockMode {
		// Special case synchronous sweep.
		// Record that no proportional sweeping has to happen.
		lock(&mheap_.lock)
		mheap_.sweepPagesPerByte = 0
		unlock(&mheap_.lock)
		// Sweep all spans eagerly.
		for sweepone() != ^uintptr(0) {
			sweep.npausesweep++
		}
		// Free workbufs eagerly.
		prepareFreeWorkbufs()
		for freeSomeWbufs(false) {
		}
		// All "free" events for this mark/sweep cycle have
		// now happened, so we can make this profile cycle
		// available immediately.
		mProf_NextCycle()
		mProf_Flush()
		return
	}

	// Background sweep.
	lock(&sweep.lock)
	if sweep.parked {
		sweep.parked = false
		ready(sweep.g, 0, true)
	}
	unlock(&sweep.lock)
}
```
8. 写屏障, 编译期在Store、Move 和 Zero 操作中加入写屏障的汇编代码，一大堆汇编代码懒得看
```
if writeBarrier.enabled {
  gcWriteBarrier(ptr, val)
} else {
  *ptr = val
}
```