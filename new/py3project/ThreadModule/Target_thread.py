# coding=utf-8
import threading
import time
k =1

def walk(n):
           global k
           k = k+n
           k=  k-n
           print "我是悟空||菩萨在此"
def run(n):
        for j in range(1,9):
            walk(n)
if __name__ == "__main__":

        t1  = threading.Thread(target=run,name='thread_mo1',args=(5,))
        t2 = threading.Thread(target=run,name="thread_no2",args=(4,))
        t1.start()
        t2.start()
        t1.join()
        t2.join()
        print k
    # t1.start()
    # t2 = threading.Thread(target=Test().walk(2),name="thread2")
    # t2.start()
