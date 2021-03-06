1. 内核调用
    - x内核中设置了一组用于实现各种系统功能的子程序，称为系统调用。。系统调用由操作系统核心提供，运行于核心态;而普通的函数调用由函数库或用户自己提供，运行于用户态。
2. TCP的可靠性传输
    - 序列号和确认应答信号
    - 超时重传（考虑RTT及其偏差）
    - 连接管理（3握4挥）
    - 以段为单位进行数据包的发送
    - 滑动窗口控制
    - 流量控制 （控制发送者）
    - 拥塞控制 （控制网络）
3. 浏览器url
    - 输入地址
    - 浏览器查找域名的 IP 地址
    - 浏览器向 web 服务器发送一个 HTTP 请求
    - 服务器的永久重定向响应
    - 服务器处理请求
    - 服务器返回一个 HTTP 响应
    - 浏览器显示 HTML
    - 浏览器发送请求获取嵌入在 HTML 中的资源（如图片、音频、视频、CSS、JS等等）
4. 高并发
    - 页面静态化
    - 异步
    - 缓存预热
    - 限流
    - 熔断
    - 降级
5. 进程通信
    - 管道
    - 消息队列
    - 信号
    - 信号量（锁机制）
    - 共享内存
    - socket
6. 分布式锁
    - 互斥性:和我们本地锁一样互斥性是最基本，但是分布式锁需要保证在不同节点的不同线程的互斥。
    - 可重入性:同一个节点上的同一个线程如果获取了锁之后那么也可以再次获取这个锁。
    - 锁超时:和本地锁一样支持锁超时，防止死锁。
    - 高效，高可用:加锁和解锁需要高效，同时也需要保证高可用防止分布式锁失效，可以增加降级。
    - 支持阻塞和非阻塞:和ReentrantLock一样支持lock和trylock以及tryLock(long timeOut)。
    - 支持公平锁和非公平锁(
7. 分布式锁lock
    - lock
    - trylock()
    - trylock(timeout)
    - unlock() 锁删除
8. 乐观锁 （https://www.cnblogs.com/kismetv/p/10787228.html）
    - CAS（compare and swap） （ABA问题、高竞争开销、功能限制）
    - 版本号 （高竞争开销；功能限制：只能保证单个变量的原子性，query的时候是针对表1而update的时候是针对表2）
9. 分布式锁安全问题
    - client1获得锁，程序STW后，锁超时，client2又获得锁
    - 时钟发生跳跃
    - 长时间的网络I/O
10. 字节对齐
    - 效率
    - 存储
    - 取决于硬件&操作系统
11. 统计函数执行次数的方法（切面编程）
```
from functools import wraps

def logit(func):
    @wraps(func)
    def with_logging(*args, **kwargs):
        print(func.__name__ + " was called")
        return func(*args, **kwargs)
    return with_logging
```
12. 为何redis使用skiplist作为zset的实现而不是红黑树
    - 按照区间查找数据，效率更高
    - 代码简单易懂
    - 灵活，可改变索引构建策略来平衡skiplist
    - 插入、删除操作更简单、更快（概率均衡技术） （红黑树也都是logn）
    - 天然有序，flush到磁盘的时候更快