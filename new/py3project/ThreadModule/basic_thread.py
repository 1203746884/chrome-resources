# coding=utf-8
import threading
import time

"""
Python通过两个标准库thread和threading提供对线程的支持。thread提供了低级别的、原始的线程以及一个简单的锁。
threading模块提供的其他方法：
        threading.currentThread(): 返回当前的线程变量。
        threading.enumerate(): 返回一个包含正在运行的线程的list。正在运行指线程启动后、结束前，不包括启动前和终止后的线程。
        threading.activeCount(): 返回正在运行的线程数量，与len(threading.enumerate())有相同的结果
"""
"""
Thread类提供了以下方法:
    run(): 用以表示线程活动的方法。
    start():启动线程活动。
    join([time]): 等待至线程中止。这阻塞调用线程直至线程的join() 方法被调用中止-正常退出或者抛出未处理的异常-或者是可选的超时发生。
    isAlive(): 返回线程是否活动的。
    getName(): 返回线程名。
    setName(): 设置线程名。
"""
# 生成线程锁，要用过来取
mutex = threading.Lock()
class TestTreading(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
    """重写父类thread的run()方法,此方法一旦生成线程对象自动调用"""
    def run(self):
        """开始上锁"""
        mutexFlage = mutex.acquire()
        """判断上锁ok,你们一个一个来，放心去和菩萨说吧，在说的时候另外一个猴子不会吵你说话了"""
        if mutexFlage:
            for i in range(5):
                print "菩萨我是真悟空{}......--{}|菩萨坐在此地|".format(self.getName(),time.asctime())
                print threading.current_thread,threading.activeCount()
        """事情完了解除锁让别的线程用，哪个线程需要资源可以用了，本线程用完了,不然就blocked阻塞，形成死锁了"""
        mutex.release()
if __name__ =="__main__":
    for i in range(10):
        t = TestTreading()
        t.start()
