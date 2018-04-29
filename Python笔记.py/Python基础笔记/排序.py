#普通排序
list1 = [3,4,5,6,1,2,8]
list2 = sorted(list1,reverse=False) #升序
list22 = sorted(list1,reverse=True) #降序
print(list2)
print(list22)

#绝对值排序
list3 = [3,4,-5,6,1,2,-8]
list4 = sorted(list3,key=abs)
print(list4)