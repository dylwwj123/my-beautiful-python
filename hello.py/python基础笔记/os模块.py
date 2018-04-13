import os

#获取操作系统类型 nt - windows  posix - linux,unix,mac
# print(os.name)

#获取详细信息
# print(os.uname())

#获取操作系统中的所有环境变量
# print(os.environ)

#获取指定环境变量
# print(os.environ.get("PATH"))

#获取当前目录路径 . / a /
# print(os.curdir)

#获取当前工作目录
# print(os.getcwd())

#获取指定目录下所有的文件 list格式
# print(os.listdir(r"/Users/wukaihao/Desktop/python/hello.py"))

#在当前目录下创建/删除新目录
# os.mkdir("nonono")
# os.rmdir("nonono")

#获取文件属性
# print(os.stat("/Users/wukaihao/Desktop/python/hello.py/基础"))

#重命名
# os.rename("/Users/wukaihao/Desktop/python/hello.py/基础","/Users/wukaihao/Desktop/python/hello.py/python基础笔记")

#删除文件
#os.remove("")