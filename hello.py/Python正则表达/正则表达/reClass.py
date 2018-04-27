import re

#https://www.jianshu.com/p/5b7adc5403c5

r'''
re.match(pattern,string,flasgs=0)
pattern:匹配的正则表达式
strig:要匹配的字符串
flags:标志位，控制表达式匹配方式
re.I :忽略大小写
re.L :本地化识别
re.M :多行匹配
re.S :使.匹配包括换行符在内的有所字符
re.U :根据unicode字符集解析字符 影响\w \W \b \B
re.X :使我们灵活理解正则

尝试从字符串的起始位置匹配一个模式,如果不是起始位置匹配成功的话,返回none
'''
print(re.match("www","www.baidu.com",flags=0))


r'''
re.search(pattern,string,flasgs=0)
扫描整个字符串，并返回第一个成功的匹配
'''
print(re.search("w","bawidu.cowm",flags=0))


r'''
re.findall(pattern,string,flasgs=0)
扫描整个字符串，返回结果列表
'''
print(re.findall("asd","baadasdwidwu.coAsdwm",flags=re.I))


r'''
. 匹配除换行符意外的任意字符
[0123456789] []字符集合.匹配括号里任意的字符
[a-z] 匹配小写字符
[A-Z] 匹配大写字符
[0-0] 匹配任意数字
[0-9a-zA-Z] 匹配任意字符
[0-9a-zA-Z_] 匹配任意字符加下划线
[0-9a-zA-Z] 匹配任意字符
[^a] 匹配这个意外任意字符

\d 匹配数字
\D 匹配非数字
\w 匹配任意字符加下划线
\W 匹配非任意字符加下划线
\s 匹配任意空白符 空格 回车 制表 换行
\S 匹配非任意空白符

^ 行首匹配 在[]里不是一个意思
$ 行位匹配
\A只匹配整个字符串的开头
'''
print(re.findall(".","aaabawidu.cowm",flags=0))

print(re.findall("[0-9]","aaa3b5a6widu.cowm",flags=0))

print(re.findall("[sb]","aaa3b5a6wsbidu.cowm",flags=0))

print(re.findall("[a-z]","aaAAAAAA.cowm",flags=0))

print(re.findall("[A-Z]","aaAAAAAA.cowm",flags=0))

print(re.findall("[0-9a-zA-Z]","aaAAAAAA11111111.cowm",flags=0))

print(re.findall("[^a]","aaa123bbb",flags=0))

print(re.findall("\d","aaa123bbb",flags=0))

print(re.findall("\D","aaa123bbb",flags=0))


#QQ
re_qq = re.compile(r"[1-9]\d{5,9}$]")
print(re_qq.search("123124124"))