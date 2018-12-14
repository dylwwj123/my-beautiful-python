import time;  # 引入time模块

'''
UTC (世界协调时间)：世界标准时间
中国 UTC+8 东八区
DST 夏令时: 一种节约能源 人为规定时间制度 在夏季调快一个小时
'''

time1 = time.time()
print ("UTC世界的时间戳为:",time1)

time2 = time.gmtime()
print ("UTC世界的标准时间元组:",time2)

time3 = time.localtime(time1)
print ("本地当前的标准时间元组:",time3)

time4 = time.mktime(time3)
print ("本地时间的时间戳:",time4)

time5 = time.asctime(time3)
print ("本地时间转为字符串",time5)

time6 = time.ctime(time4)
print ("本地时间戳转为字符串",time6)

time7 = time.strftime("%Y-%m-%d %H:%M:%S")
print("常用的时间表达字符串",time7)

#cpu执行时间
#unix 始终返回全部运行时间
#window 从第二次开始 都是以第一次调用此函数的开始时间戳为基数
# print(time.clock())
# print(time.clock())
# print(time.clock())

#性能测试
# sum = 0
# for ii in range(111):
#     sum += 1
#
# print(time.clock())

#延迟执行
# time.sleep(2)
# print("qq")


import datetime;  # 引入time模块
'''
datetime 比 time 高级了不少

'''

print(datetime.datetime.now())

#时间相减
d1 = datetime.datetime(2000,10,1,10,29,25,123456)
d2 = datetime.datetime.now()
d3 = d2 - d1
print(d3)

#日历
import calendar

# print(calendar.month(2018,4))

# print(calendar.calendar(2018))

#判断闰年
print(calendar.isleap(2000))
