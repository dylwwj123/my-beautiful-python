import os
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

#读取path下的文件
filePath = os.listdir(path1)
print(filePath)

#循环处理每一个文件
star = time.time()
for fileName in filePath:
    copyFile1(os.path.join(path1,fileName),os.path.join(topath1,fileName))

end = time.time()
print("耗时: %.2d" %(end-star))
