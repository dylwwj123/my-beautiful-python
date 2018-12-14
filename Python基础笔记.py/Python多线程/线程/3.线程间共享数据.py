import threading

num = 0

#线程锁
lock = threading.Lock()

def run111(n):

    print("子线程（%s）启动" %(threading.current_thread().name))

    global num
    for i in range(10000000):
        # 锁 当线程1执行 会上锁， 当线程2过来 发现线程1上锁 会堵塞 等待线程1解锁释放
        # 确保了这段代码只能由一个线程从头到尾的完整执行
        # 阻止了多线程的并发执行，包含锁定代码其实是单线程模式执行，所以效率降低了
        # 由于可以存在多个锁，不同线程持有不同的锁，并试图获取其他的锁，可能做成死锁，导致多个线程挂起。只能靠操作系统强制终止

        #手动上锁 解锁
        # lock.acquire()
        # try:
        #     num += n
        #     num -= n
        # finally:
        #     lock.release()

        #自动上锁 解锁
        with lock:
            num += n
            num -= n


    print("子线程（%s）结束" %(threading.current_thread().name))

if __name__ == '__main__':
    print("主线程（%s）启动" %(threading.current_thread().name))

    t1 = threading.Thread(target=run111, name="run111Thread", args=(6,))
    t2 = threading.Thread(target=run111, name="run222Thread", args=(9,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("主线程（%s）结束" %(threading.current_thread().name))
    print(num)
