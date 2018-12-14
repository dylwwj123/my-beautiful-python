
# 10进制字符串 转 二进制整形
print(int("1010",base = 2))

# 10进制转二进制自定义函数
def intBase2(str):
    return int(str,base = 2)

print(intBase2("1010"))

#引入模块
import functools

functools_Int = functools.partial(int,base = 2)

print(functools_Int("1010"))