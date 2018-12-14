#创建一维数组
tuple1 = (1,2,3)
print("tuple1 =",(tuple1))

#数组下标取元素
tuple2 = (1,2,3)
print("tuple2 =",tuple2[1])

#数组下标取最后一个元素
tuple3 = (1,2,3)
print("tuple3 =",tuple3[-1])

#数组删除
tuple4 = (1,2,3)
del(tuple4)
# print("tuple4 =",tuple4)

#数组相加  得新的数组
tuple5 = (1,2,3)
tuple6 = (4,5,6)
print("tuple5+tuple6 =",tuple5+tuple6)

#数组重复
tuple7 = (1,2,3)*3
print("tuple7 =",tuple7)

#判断数组中是否存在某值
tuple8 = (1,2,3)
print("tuple8 =",3 in tuple8)

#数组截取
tuple9 = (1,2,3,4,5,6)
print("tuple9 =",tuple9[2:4])

#创建二维数组
tuple10 = ((1,2,3),(1,2,3),(1,2,3))
print("tuple10 =",tuple10)
print("tuple10 =",tuple10[1][1])

#元素的个数
tuple11 = (1,2,3)
print("tuple11 =",len(tuple11))
#元素的最大值
print("tuple11 =",max(tuple11))
#元素的最小值
print("tuple11 =",min(tuple11))

#数组安全!!!!!!!!!!! 不可改

for i in (1,2,3,4):
    print(i)

for i in [1,2,3,4]:
    print(i)
