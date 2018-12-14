import random, time, multiprocessing,os

def run1(name):

    print("%s---子进程开始---%s" %(name,os.getpid()))

    startTime = time.time()

    time.sleep(random.choice([1,2,3]))

    endTime = time.time()

    print("%s子进程结束---%s   用时--%.2f" %(name,os.getpid(),(endTime-startTime)))

if __name__ == '__main__':

    print("父进程开始")

    #进程池
    #pool默认是cpu核心数 有值是可以同时执行进程的数量
    poo = multiprocessing.Pool(1)

    for i in range(1,10):
        #创建进程，放入进程池同意管理
        poo.apply_async(run1, args=(i,))

    #关闭之后就不能继续添加新的进程了
    poo.close()
    #进程池对象调用的join,等进程池执行完后在执行父进程
    poo.join()

    print("父进程结束")
