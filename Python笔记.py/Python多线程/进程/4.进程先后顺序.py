from multiprocessing import Process
import time
import os


def run1(str):

    print("启动子进程11")

    time.sleep(3)

    print("结束子进程11")


def run2(str):

    print("启动子进程22")

    time.sleep(1)

    print("结束子进程22")


if __name__ == '__main__':

    print("启动父进程")

    p1 = Process(target = run1, args=("11",))

    p1.start()

    p2 = Process(target = run2, args=("11",))

    p2.start()

    #父进程的结束不会影响子进程，
    # print("结束父进程")

    #让父进程等待子进程结束在结束父进程
    p1.join()
    p2.join()
    print("结束父进程")
