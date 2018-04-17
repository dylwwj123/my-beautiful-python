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

#所有关键字
import keyword
print(keyword.kwlist)

# zip 两个数组转dict
A0 = dict(zip(('a','b','c','d','e'),(1,2,3,4,5)))

A1 = range(10)

A2 = [i for i in A1 if i in A0]

A3 = [A0[s] for s in A0]
# for s in A0:
#     print(A0[s])

A4 = [i for i in A1 if i in A3]

A5 = {i:i*i for i in A1}

A6 = [[i,i*i] for i in A1]

print(A0)
print(A1)
print(A2)
print(A3)
print(A4)
print(A5)
print(A6)