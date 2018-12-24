# coding=utf-8
import threading
import time


mutex = threading.Lock()
class TestTreading(threading.Thread):
    def __init__(self,id):
        threading.Thread.__init__(self)
        self.id =id
    """重写父类thread的run()方法,此方法一旦生成线程对象自动调用"""
    def run(self):
        """开始上锁"""
        mutexFlage = mutex.acquire()
        """判断上锁ok,你们同时开始在规定时间考试，都来做加法运算，给你们参数给的不同避免抄袭做自己的结果"""
        if mutexFlage:
            for i in range(10000):
                print self.add(),self.getName(),time.asctime()


        """事情完了解除锁让别的线程用，哪个线程需要资源可以用了，本线程用完了,不然就blocked阻塞，形成死锁了"""
        mutex.release()
    def add(self):
        x=self.id
        for i in range(101):
            x=x+i
        return x
if __name__ =="__main__":
    threads=[TestTreading(i)for i in range(10)]
    for t in threads:
        t.start()
    for t in threads:
        t.join()
    print "main thread closed"