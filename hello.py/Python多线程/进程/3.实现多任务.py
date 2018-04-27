'''
multiprocessing 跨平台多进程的三方库
提供一个process类来代表一个进程对象
'''

from multiprocessing import Process
import time
import os

def run(str):
    while True:
        #pid 进程id号  ppid子进程的主进程id
        print("%s  processId==%s  getppid==%s" %("子线程启动",os.getpid(),os.getppid()))
        time.sleep(1)

if __name__ == '__main__':

    #创建一个子进程
    #target 进程执行的任务
    #args 传参数
    p1 = Process(target = run, args=("11",))
    #启动进程
    p1.start()

    while True:
        print("主进程启动 processId==%s" %(os.getpid()))
        time.sleep(1)