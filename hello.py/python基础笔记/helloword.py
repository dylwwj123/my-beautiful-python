#单行输出函数
print ("\nhello python")

#多行,段落输出函数
print("""
我是第一行
我是第二行
我是第三行
我是第四行
""")

#三个单引号多行注释
'''
print ("hello python")
'''

#python严格区分大小写
#python代码要严格对齐

#/除法 //整除
print (5/2)
print (5//2)

import time;  # 引入time模块
ticks = time.time()
print ("当前时间戳为:", ticks)
localtime = time.localtime(time.time())
print ("本地时间为 :", localtime)
localtime = time.asctime( time.localtime(time.time()) )
print ("本地时间为 :", localtime)
print (time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
print (time.strftime("%a %b %d %H:%M:%S %Y", time.localtime()))
# 将格式字符串转换为时间戳
a = "Sat Mar 28 22:24:24 2016"
print (time.mktime(time.strptime(a,"%a %b %d %H:%M:%S %Y")))

#所有关键字
import keyword
print(keyword.kwlist)

while 1:
    print("1")
    time.sleep(0.1)