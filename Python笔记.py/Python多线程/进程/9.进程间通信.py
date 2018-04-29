import multiprocessing
import os
import time

def white(q):
    print("写子线程启动 %s" %(os.getpid()))
    for cha in ["a","b","c","d"]:
        q.put(cha)
        time.sleep(1)
    print("写子线程结束 %s" %(os.getpid()))


def red(q):
    print("读子线程启动 %s" % (os.getpid()))
    while True:
        value = q.get(True)
        print("value = %s" %(value))
    print("读子线程结束 %s" % (os.getpid()))


if __name__ == '__main__':

    #父进程创建队列，并传递给子进程
    q = multiprocessing.Queue()

    wp = multiprocessing.Process(target=white, args=(q,))

    rp = multiprocessing.Process(target=red, args=(q,))

    wp.start()

    rp.start()

    wp.join()

    #进程里是个死循环，无法等待其结束，只能强行结束
    rp.terminate()

    print("father")
