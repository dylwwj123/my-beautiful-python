import os
import multiprocessing
import time

def copyFile1(rPath, rWrite):
    fr = open(rPath, "rb")
    fw = open(rWrite, "wb")
    context = fr.read()
    fw.write(context)
    fr.close()
    fw.close()

path1 = "/Users/wukaihao/Desktop/python/hello.py/Python多线程/进程/file"
topath1 = "/Users/wukaihao/Desktop/python/hello.py/Python多线程/进程/tofile"

if __name__ == '__main__':

    # 读取path下的文件
    filePath = os.listdir(path1)

    poo = multiprocessing.Pool()

    star = time.time()

    for fileName in filePath:
        poo.apply_async(copyFile1, args= (os.path.join(path1, fileName), os.path.join(topath1, fileName)))

    poo.close()
    poo.join()
    end = time.time()
    print("耗时: %.2d" % (end - star))