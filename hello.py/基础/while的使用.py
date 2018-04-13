#while循环
num1 = 1
while num1<6:
    print(num1)
    num1 += 1

num2 = 1
sum2 = 0
while num2<101:
    sum2 += num2
    num2 += 1

print("sum2 = %d" %(sum2))

str1 = "你是真的牛b"
index1 = 0
while index1<len(str1) :
    print("str1[%d] = %s" %(index1,str1[index1]))
    if index1 == 1 :
        print("*"*20)
    index1 += 1

#for循环
list1 = [1,2,3,4,5,6,7,8,9]
for i in list1:
    print(i)

for i in range(1,10,2):
    print(i)

for i1,i2 in enumerate([1,2,3,4,5]):
    print(i1,i2)

#break 跳出循环 只能跳出距离它最近的那一层循环
# for i in range(1,10):
#     print("break",i)
#     for ii in range(1,3):
#          if ii == 2:
#              print("break222", ii)
#              break
#          else:
#              print("break222!!")
#     if i == 5:
#         break

#continue 跳过当前循环剩下的语句 然后开始下一次循环
for i in range(1,10):
    print("continue",i)
    if i == 5:
        continue
    print("s")
    print("b")