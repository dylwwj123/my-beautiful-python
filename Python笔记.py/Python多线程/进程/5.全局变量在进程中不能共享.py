from multiprocessing import Process
from time import sleep

num = 100

def run1():

    print("子进程开始")

    global num
    num += 1

    print("子进程结束---%d" %(num))


def run2():

    print("子进程开始")

    global num
    num += 2

    print("子进程结束---%d" %(num))


if __name__ == '__main__':

    print("父进程开始")

    p1 = Process(target = run1)
    p1.start()
    p1.join()

    p2 = Process(target = run2)
    p2.start()
    p2.join()

    #在子进程中修改的全局变量对父进程中的全局变量没有影响
    #在创建子进程时对全局变量做了一个备份，父进程中的num与子进程的num是两个变量
    print("父进程结束---%d" %(num))
