#与list的区别
#插入和查找的速度极快,不会随着key,value的增加而变慢。
#需要占用大量的内存,内存浪费多。

dict1 = {"name":"王","age":20,"height":180}
print(dict1)
print(dict1.get("name"))
print(dict1.get("age"))
print(dict1.get("height"))

if dict1.get("height") != None:
    print("身高真的")
else:
    print("身高假的")

# 添加 有的话覆盖
dict1["tizhong"] = 130
dict1["age"] = 22
print(dict1)

# 删除 dict的pop是根据key删除 list的pop是根据下标删除
dict1.pop("age")
print(dict1)

# 遍历
#(1)
for key in dict1:
    print(key,dict1[key])

#(2)
for value in dict1.values():
    print(value)

#(3)
for key,value in dict1.items():
    print(key,value)


# 类似dict 是一组key的集合 不存储value
# 也是无序 但是 无重复的集合
set1 = set([1,2,3,4,5,1,1,1])
set11 = set({1,2,3,4,5,1,1,1})
set111 = set((1,2,3,4,5,1,1,1))
print(set1)

# 添加 不可添加可变元素
set1.add(6)
set1.add((1,2))
print(set1)

# 打碎添加
set1.update([7,8])
set1.update({9:10})
set1.update("10")
print(set1)

# 删除
set1.remove(1)
set1.remove("1")
print(set1)

#遍历
for value in set1:
    print(value,type(value))

#交集
set2 = set([1,2,3])
set3 = set([2,3,4])

set4 = set2 & set3
print(set4)

#并集
set4 = set2 | set3
print(set4)
