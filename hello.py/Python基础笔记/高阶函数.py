#python高阶函数

#map()
#原型 map(fn,lsd)
#参数一是函数
#参数二是序列
#将传入的参数依次作用在序列中的每一个元素,执行的结果返回一个列表。

def char1(char):
    return {"0":0,"1":1,"2":2,"3":3,"4":4}[char]

list1 = ["3","4","2","1"]
map1   = map(char1,list1)
print(list(map1))

list2 = map(str,[1,2,3,4])
print(list(list2))


#reduce()
#原型 reduce(fn,lsd)
#参数一是函数
#参数二是列表
#将传入的参数依次作用在序列上，这个函数必须接受两个参数，把结果和下一个元素累计计算。

from functools import reduce

def mysum(x,y):
    return x+y

list2 = [1,2,3,4,5,6]

print(reduce(mysum,list2))


#filter()
#原型 reduce(fn,lsd)
#参数一是函数
#参数二是序列
#将传入的参数依次作用在序列中的每一个元素，根据返回的ture还是false决定保留改元素

def func(num):
    if num%2 == 0:
        return True
    return False

list3 = [1,2,3,4,5,6,7,8,9];

list4 = filter(func,list3)

print(list(list4))


data = [["奥奥","试试","说的"],["奥奥","试试","说的"]]

def func2(v):
    v = str(v)
    if v == "试试":
        return False
    return True

for line in data:
    m = filter(func2,line)
    print(list(m))
