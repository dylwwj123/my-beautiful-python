import threading
import time

num = 10

def run(age):

    print("子线程（%s）启动" %(threading.current_thread().name))

    time.sleep(2)

    print(num)

    print(age)

    print("子线程（%s）结束" %(threading.current_thread().name))


if __name__ == '__main__':
    #任何进程默认就会启动一个主线程。主线程可以启动子线程。
    #threading.current_thread()返回线程实例
    print("主线程（%s）启动" %(threading.current_thread().name))

    #创建子线程
    t = threading.Thread(target=run, name="runThread", args=(10111,))
    t.start()
    t.join()

    print("主线程（%s）结束" %(threading.current_thread().name))
