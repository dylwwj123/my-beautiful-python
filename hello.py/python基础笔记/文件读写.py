'''
过程:
1.打开文件
open(path,flag[, encoding][, errors])
path:文件路径
flag:打开方式
r:   只读的方式打开文件
rb:  二进制格式打开文件 只读
r+:  读写
w:   写入的方式打开文件,有文件的话会覆盖,没有则会创建一个
wb:  二进制格式打开文件 写入
w+:  读写
a:   打开文件,用于追加。如果文件存在。从最后追加。
a+:
encoding:编码方式 常用utf-8
errors:错误处理

2.读取文件内容

3.关闭文件
'''

#打开文件 没有则创建一个。
# path = open(r"/Users/wukaihao/Desktop/python/hello.py/file/qq.txt","r",encoding="utf-8")

#读取全部
# strpath1 = path.read()
# print(strpath1)

#继续读一遍全部 修改描述符的位置
# path.seek(0)
# strpath5 = path.read()
# print(strpath5)

#读取一行 包括/n
# strpath2 = path.readline()
# print(strpath2)

#读取下一行 包括/n
# strpath3 = path.readline()
# print(strpath3)

#读取所有行返回list
# strpath4 = path.readlines()
# print(strpath4)
# print(strpath4.strip())  # 把末尾的'\n'删掉

#关闭文件
# path.close()

#完整的使用过程
# try:
#     f1 = open(path,"r",encoding="utf-8")
#     print(f1)
# finally:
#     if f1:
#         f1.close()

#遇到有些编码不规范的文件，你可能会遇到UnicodeDecodeError，
#因为在文本文件中可能夹杂了一些非法编码的字符。遇到这种情况，open()函数还接收一个errors参数，
#表示如果遇到编码错误后如何处理。最简单的方式是直接忽略： errors='ignore'  忽略错误

#写文件 将信息写入缓冲区
# 然后刷新缓冲区 flush手动刷新缓冲区
# with open(r"/Users/wukaihao/Desktop/python/hello.py/file/qq1.txt","a",encoding="utf-8") as f2:
#     f2.write(r"111111111请问")

#最常用的读文件方式 with自动关闭文件
# with open(r"/Users/wukaihao/Desktop/python/hello.py/file/qq2.txt","r",encoding="utf-8") as f2:
#     print(f2.read())


# 写文件 二进制
# with open(r"/Users/wukaihao/Desktop/python/hello.py/file/qq2.txt","wb") as f2:
    # f2.write(r"qwesad请问请问223".encode("utf-8"))

#读文件 二进制
# with open(r"/Users/wukaihao/Desktop/python/hello.py/file/qq2.txt","rb") as f3:
#     print(f3.read())
    # print(type(f2.read()))
    # print((f3.read()).decode("utf-8"))


# list & tuple & dict & set 的文件操作

import pickle #数据持久化模块

dict = {"name":"sb","age":18}

# mylist = (1,2,3,4,5,"py","派森");

path = r"/Users/wukaihao/Desktop/python/hello.py/file/qq3.txt"
wf = open(path,"wb")
pickle.dump(dict,wf)
wf.close()

#读取
rf = open(path,"rb")
readlist = pickle.load(rf)
rf.close()
print(readlist)
