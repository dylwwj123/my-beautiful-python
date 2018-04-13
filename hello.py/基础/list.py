list1 = ["11",11,22,"22"] #一维列表
print(list1)
print(list1[2])

#list元素替换
list1[2]="33"
print(list1)

list2 = ["11","22"]
list3 = ["33","44"]
list4 = list2 + list3 #组合列表
print(list4)
print(list4*2) #多个相同列表
print("22" in list4) #判断列表里是否存在这个值
print("55" in list4) #判断列表里是否存在这个值
print(list4[1:3])#截取

list5 = [["11","22"],["33","44"],["55","66"]] #二维列表
print(list5)
print(list5[1][1])
print("22" in list5[0])

list5.append("77") #追加
list5.append(["88","99"])

list5.insert(0,["1010","1111"]) #插入
list5.insert(1,"12")
print(list5)

list5.pop(0) #根据下标移除
list5.remove(["88","99"]) #根据内容移除第一个
print(list5)

list5.clear() #all clean 全部滚蛋
print(list5)

list6 = [11,22,11,11,555,11]
print(list6.index(11)) #查找某个值的第一个匹配的元素
print(list6.index(11,4,7)) #指定范围查找

print("lllllllllllllen",len(list6)) #元素的个数

print(max(list6)) #最大元素
print(min(list6)) #最小元素

print(list6.count(11)) #元素出现的次数

#循环删除列表里指定的所有元素
list7 = [11,22,11,11,555,11]
index = 0
allcount = list7.count(11)

while index < allcount :
    list7.remove(11)
    print(list7)
    index += 1

list8 = [2,1,3]
list8.reverse() #列表倒序
print(list8)
list8.sort() #元素升序
print(list8)

list9 = list8 #浅拷贝 内存地址同一份 复制一个栈区指向相同的堆区
list10 = list8.copy() #深拷贝 内存地址两份 两个栈区指向两个堆
list9[1] = 100
list10[1] = 200
print(list8)
print(list9)
print(list10)

tuple1 = (1,2,3)
list11 = list(tuple1) #将元组转换成list
print(tuple1)
print(list11)