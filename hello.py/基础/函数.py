'''
函数:
在一个完整的项目中,某些功能会反复的使用。那么就将这个功能封装成函数,当我们使用这个功能的时候,直接调用函数即可。
优点:
1.简化代码得结构,增加了代码得复用度
2.如果修改某些功能或bug 需改对应的函数即可。
'''

# 无返回值的函数
def  hanshu1():
    print("wws")

hanshu1()

# 带返回值的函数
def  hanshu2(name,age):
    print("姓名 = %s , 年龄 = %d" %(name,age))

hanshu2("文帅",24)

# return 返回的值
def hanshu3(num1,num2):
    sum = num1+num2
    return sum

print(hanshu3(1,2))

# 默认参数
def hanshu3(num1=1,num2=2):
    sum = num1+num2
    return sum

print(hanshu3(5))

# 加了*号的变量存放所有未命名的变量参数
def hanshu4(num1,*args):
    print(num1)
    for num in args:
        print(num)

hanshu4("1","2","3","4")

# 生成字典
def hanshu5(**kwargs):
    print(kwargs)

hanshu5(x=1,y=2,z=3)

# 匿名函数
sum = lambda num1,num2 : print(num1,num2)
(sum("dd","bb"))

sum1 = lambda num1,num2 : num1+num2
print(sum1(11,22))