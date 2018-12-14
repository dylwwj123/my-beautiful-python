string1 = "ABCDEFGHIJKLMN"
string11 = ""
print("string1 =",string1)
print("string1 =",len(string11))

string2 = string1[1]
print("string2 =",string2)

#字符串截取
string3 = string1[:4]
string4 = string1[4:7]
string5 = string1[7:]
print("string3 =",string3)
print("string4 =",string4)
print("string5 =",string5)

string6 = "我是真的帅阿"
if "帅" in string6 :
    print("真的帅")
else:
    print("真的丑")

if "帅" not in string6 :
    print("真的帅")
else:
    print("真的丑")

int1 = 100
float1 = 100.1234567 #float默认小数点后六位 最后一位四舍五入
string7 = "妈卖批"
print("int1 = %d  float1 = %f float1 = %.3f string7 = %s" %(int1,float1,float1,string7))

print(eval("11+11"))
print(len("123456"))
print("QWEASDZXC".lower()) #大小变小写
print("qweasdzxc".upper()) #小写变大写
print("QWEASdzxc".swapcase()) #大小变小写,小写变大写
print("qweasdzxc".capitalize()) #首字母大写
print("qwe asd zxc".title()) #每个单词首字母大写
print("大傻逼".center(11,"*"))
print("大傻逼大傻逼大傻逼".count("傻逼",0,len("大傻逼大傻逼大傻逼")))
print("12312eqwe大傻逼".find("大傻逼"))
print("12312eqwe大傻逼".lstrip("123"))
print("12312eqwe大傻逼".rstrip("大傻逼"))
print("123大傻逼****123".strip("123"))

#随机生成6位验证码
import random

random_str = ""
for i in range(0,6):
    random_int = random.randint(0, 9)
    random_str = random_str + str(random_int)

print("%s" %(random_str))

#把指定字符变成空字符串
string8 = "qwe*qwe********we**w"
print("splitsplitsplit = ",string8.split("*"))

list8 = string8.split("*")
allcount = list8.count("")

index = 0
while index < allcount :
    list8.remove("")
    index += 1
print(list8)

#字符串全部替换
string12 = "11111111111222222222"
string12 = string12.replace("1","2")
print(string12)

#编解码
string13 = "qqq 刷 阿萨德啊"
print(string13.encode("utf-8"))
print((string13.encode("utf-8")).decode("utf-8"))

