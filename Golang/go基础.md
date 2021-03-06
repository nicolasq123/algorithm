1. 空切片与nil切片的区别
    - 1.nil切片和空切片指向的地址不一样。nil空切片引用数组指针地址为0 
    - 2.空切片的引用数组指针地址是有的，且固定为一个值
2. 字符串转成byte数组，会发生内存拷贝吗
    - 会, 底层结构不一样，需要用unsafe.Pointer转

```
type StringHeader struct {
 Data uintptr
 Len  int
}
```
3. 翻转含有中文、数字、英文字母的字符串
    - str强转[]rune
4. 拷贝大切片一定比小切片代价大吗
    - 一样
```
type SliceHeader struct {
 Data uintptr
 Len  int
 Cap  int
}
```

5. map的iterator是否安全？能不能一边delete一边遍历
   - 安全， 能。删除操作仅仅将对应的tophash[i]设置为empty，并非释放内存。

6. closed 状态的chann是读安全的，写会panic
7. 向nil 值状态的chann 读写，都会永远阻塞
8. 方法接收者是类型（T），接收者只是原对象的值复制，在方法中修改接收者不会修改原始对象的值；如果方法接收者是指针类型（*T），是对原对象的引用，方法中对其修改当然是原对象修改。
```
type data struct {
	num   int
	key   *string
	items map[string]bool // 引用类型，所以副本也可以修改
}

func (this *data) pmethod() {
	this.num = 7
}

func (this data) vmethod() {
	this.num = 8
	*this.key = "xxx"
	this.items["vmethod"] = true
}
```
9. 如果实现了接收者是值类型的方法，会隐含地也实现了接收者是指针类型的方法。
10. json包变量不加tag会怎么样
    - 小写private不处理
    - 无tag就是变量名，有tag使用tag
11. 切片初始化
    - make([]type, len)  make([]type, len， cap)
    - s := make([]int, 10) 零切片
    - var s1 []int; var s2 = []int{}; var s3 = make([]int, 0); var s4 = *new([]int); s1 s4nil切片， s2 s3空切片
12. map触发扩容的时机，满足什么条件时扩容
    - 装载因子超过阈值，源码里定义的阈值是 6.5 （元素太多，需要扩容。 此情况新bucket*2）
    - overflow 的 bucket 数量过多 （拉链法hashtable， 防止退化成链表。 开辟新bucket空间）
13. map扩容策略是什么
    - 比较复杂，渐进式把旧bucket数据搬迁到新bucket
14. 为什么遍历 map 是无序的
    - map扩容后，发生搬迁，顺序就变了
    - 新老bukcet搬迁，map会处于一个中间未搬迁完的中间状态
    - 每次都是从一个随机值序号的 bucket 开始遍历（go机制， 防止误解），使你是一个写死的map，遍历顺序也是随机的
15. map操作 （https://zhuanlan.zhihu.com/p/66676224）
    - range
    - update/insert
    - delete,找到对应位置后，对 key 或者 value 进行“清零”操作. 将count--
    - 边遍历边写，或者边遍历边删除，会panic
16. golang slice (https://www.cnblogs.com/qcrao-2018/p/10631989.html)
17. 为什么 nil、空slice 可以直接 append
    - 调用append函数来获得底层数组的扩容

```
type slice struct {
	array unsafe.Pointer // 元素指针
	len   int // 长度 
	cap   int // 容量
}
```
18. new,make区别
    - new(T)，分配空间，且为0值，返回T类型指针
    - make(T, args)只能用于slice,map,channel。返回始化之后的T
19. channel (https://qcrao.com/2019/07/22/dive-into-go-channel/)
    - func makechan(t *chantype, size int) *hchan 。 返回的是*hchan

```
type hchan struct {
	qcount   uint           // total data in the queue
	dataqsiz uint           // size of the circular queue
	buf      unsafe.Pointer // points to an array of dataqsiz elements
	elemsize uint16
	closed   uint32
	elemtype *_type // element type
	sendx    uint   // send index
	recvx    uint   // receive index
	recvq    waitq  // list of recv waiters
	sendq    waitq  // list of send waiters

	// lock protects all fields in hchan, as well as several
	// fields in sudogs blocked on this channel.
	//
	// Do not change another G's status while holding this lock
	// (in particular, do not ready a G), as this can deadlock
	// with stack shrinking.
	lock mutex
}
```
20. 优雅关闭chan
    - 一个 sender，一个 receiver. sender关闭
    - 一个 sender， M 个 receiver. sender关闭
    - N 个 sender，一个 reciver. recv通过另外一个chan通知sender退出，recv退出，最后gc代劳回收dataChan
    - N 个 sender， M 个 receiver. 一个中间人来关闭topCh.senders和recvs退出，最后gc代劳回收dataChan

```
stopCh := make(chan struct{})
toStop := make(chan string, 1) // 缓冲型，避免丢失第一个信号

go func() {
    <-toStop
    close(stopCh)
}()

go func() {
    for {
        if xxxx {
            // 满足条件就退出
            select {
            case toStop <- "receiver#" + id:
            default:
            }
            return
        }
    }
    // do sth;
}
```

21. 3种线程安全map
    - 读写锁
    - 分片加锁，N个map，N个锁，根据key hash
    - sync.map

22. Golang for循环里append。
    - go语法糖在for循环前记录了len，不会死循环。 这种写法应被严厉禁止
    - 其他语言里for循环修改迭代器可能导致迭代器失效
23. for select时，如果通道已经关闭会怎么样
    - 一直读出零值和false。可代码处理退出当ok==false
24. 内存逃逸
    - 发生在编译期
    - 在方法内把局部变量指针返回
    - 发送指针或带有指针的值到 channel 中
    - 在一个切片上存储指针或带指针的值
    - slice 的背后数组被重新分配了，因为append时可能会超出其容量(cap)
    - 在 interface 类型上调用方法
```
func foo(s string) *A {
	tmp := A{}
	a := &tmp
	a.s = s
	return a //返回局部变量tmp的地址,在C/C++语言中妥妥野指针，但在go则ok，但a会逃逸到堆
}
```

25. resp.Body.Close() 未执行会导致泄露一个read goroutine 和一个写 goroutine
26. 对已经关闭的的 chan 进行读写，会怎么样
    - 读完管道的数据，然后连续读到"零值,false"
    - 写会panic
27. 对未初始化的的 chan 进行读写，会怎么样
    - 阻塞
28. goroutine 泄露
    - 长时间读、写阻塞
    - 死循环
    - chan有读无写，chan有写无读，select所有case一直都不满足
29. go垃圾回收
    - 三色标记法配合写屏障和辅助GC
    - 三色标记法（标记清除的增强版）
        - 黑色，代表根节点或者已扫描完的节点，该节点的子节点也被扫描完；
        - 灰色，代表已扫描完的节点，该节点的子节点存在未被扫描的情况；
        - 白色，代表未被扫描的节点。
30. GC如何工作
    - mark
        - 初始化GC，开启写屏障write barrier，辅助GC
        - 扫描所有root对象，全局指针和goroutine(G)栈
    - 标记完成， 重新扫描(re-scan)全局指针和栈。
    - Sweep: 按照标记结果回收所有的白色对象，该过程后台并行执行
    - Sweep Termination: 对未清扫的span进行清扫, 只有上一轮的GC的清扫工作完成才可以开始新一轮的GC。
31. 写屏障（Write Barrier）
    - 赋值器的写屏障，使赋值器在进行指针写操作时，能够“通知”回收器，防止被错误回收
32. 辅助GC
    - GC速度跟不上用户分配速度时，暂停用户线程/协程，叫做辅助GC
33. 如何进行GC调优
    - 减少显示分配
    - 减少隐示分配(string与[]byte转话，字符串相加等等)
    - 主动释放. 不使用的置为nil
    - 主动调用runtime.GC()
34. var _ io.Writer = (*myWriter)(nil)
    - 编译期自动检测类型是否实现接口
35. GMP模型 
    - [GMP](https://zboya.github.io/post/go_scheduler/?hmsr=toutiao.io&utm_medium=toutiao.io&utm_source=toutiao.io)
    - Goroutine, 调度系统的最基本单元，存储了stack、状态、任务函数
    - Processor，代表线程M的执行的上下文，拥有G对象列表、链表、cache和状态
    - Machine，M代表真正的执行计算资源，可以认为是OS线程
36. 调度
    - go func() 语气创建G。
    - 将G放入P的本地队列（或者平衡到全局队列）。
    - 唤醒或新建M来执行任务。
    - 进入调度循环
    - 尽力获取可执行的G，并执行
    - 清理现场并且重新进入调度循环
37. 动图图解，GMP里为什么要有P (https://mp.weixin.qq.com/s?__biz=Mzg5NDY2MDk4Mw==&mid=2247486385&idx=1&sn=522c090c31ad35017d545445b9017420&source=41#wechat_redirect)
    - Go 1.1版本之前，其实用的就是GM模型
    - GM模型，每次切换G都要去全局G队列里拿G，需要消耗锁
    - GPM模型，每次切换G只需要去P的本地G队列拿G，减少锁消耗
38. 两个interface{} 能不能比较
    - 会比较底层类型和值
39. 必须要手动对齐内存的情况
    - 32bit平台上，原子操作 64bit 指针，必须要手动对齐，否则panic
40. go栈扩容和栈缩容，连续栈的缺点
    - 函数栈会扩缩容(2倍or1/2倍) （早期版本使用的是分段栈机制）
    - 连续栈导致更多的虚拟内存碎片
41. 怎么访问私有成员
    - 地址访问（高风险，严禁使用）
42. 问题排查&性能优化
    - trace (go早期版本查看view有问题，需要用docker跑)
    - pprof
43. 源码阅读 
    - sync.map (https://qcrao.com/2020/05/06/dive-into-go-sync-map/)
    - net/http
    - mutex (https://mp.weixin.qq.com/s/MntwgIJ2ynOAdwnypWUjZw)
        - 休眠原语runtime_Semacquire
        - 无冲突，直接锁；有冲突开始自旋；有冲突，休眠；
    - channel
    - context
        - cancel实际上是close(c.done), remove children
    - select实现原理
        - no cases,no def,直接永久block()
        - 1 case,no def, 直接转成if语句。（ch==nil该G会永久block）
        - some cases, fastrandn随机选
    - 内存管理
        - mheap, mheap.spans 存储span和page信息；  mheap.bitmap 存储着各个 span 中对象的标记信息；mheap.arena_start将要分配给应用程序使用的空间
        - mcentral，管理不同sizeclass的span（这种方式可以避免出现外部碎片）
        - mcache，每一个 mcache 和每一个处理器(P) 是一一对应的，在mcache里申请内存是不需要锁消耗的。（这点类似于GMP结构中的P设计）
        - zero size。 [0]int, struct{}等会返回一个固定的内存地址。
        - tiny对象的分配，16B的object用以复用分配
        - 大对象的分配，直接从mheap上获取，如果mheap上有剩余空间，上述分配是不需要进入内核态的，速度会更快
    - GC
        - 三色，写屏障，辅助GC
    - timer
        - 最多64桶，桶内最小堆维护timers，休眠到下一次触发时间就唤醒当前桶的g
44. plan9汇编
    - 与x86汇编有所区别，了解即可，需要时再深入了解