import multiprocessing
import time
import os

class MyProcess(multiprocessing.Process):

    def __init__(self, name):
        multiprocessing.Process.__init__(self)
        self.name = name

    def run(self):
        print("子线程(%s--%s)启动" %(os.getpid(),self.name))
        time.sleep(3)
        print("子线程(%s--%s)关闭" %(os.getpid(),self.name))
