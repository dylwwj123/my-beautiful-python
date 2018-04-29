import itertools
import time

#排列
mylist1 = list(itertools.permutations("123456", 3))
print("\n排列: %s" %(mylist1))

#组合
mylist2 = list(itertools.combinations([1, 2, 3, 4], 3))
print("\n组合: %s" %(mylist2))

#排列组合
mylist3 = list(itertools.product("1234567890aqwe",repeat=2))
print("\n排列组合: %d" %(len(mylist3)))

#一个一个执行
mylist4 = ("".join(x) for x in itertools.product("0123456789aqwe",repeat=2))
print("\n暴力组合: %s" %(next(mylist4)))

while True:
    try:
        time.sleep(0.5)
        str = next(mylist4)
        print(str)
    except StopIteration as e:
        break
