import re

r'''
      .  匹配任意字符                    *  匹配前一个字符0次或多次       + 匹配前一个字符一次或多次
      ?  匹配前一个字符0次或1次           ^  匹配字符串开头              $ 匹配字符串末位
      () 匹配括号内的表达式，也表示一个组   \s 匹配空白字符               \S 匹配非空白字符
      \d 匹配数字 等于[0-9]              \D 匹配任何非数字 等于[^0-9]   \w 匹配字母数字 等于[A-Za-z0-9_]
      \W 匹配非字母数字等于[^A-Za-z0-9_]  [] 表示一组字符
      
      \d{3}\s+\d{3,8}：
      \d{3}表示匹配3个数字，例如'010'；    
      \s可以匹配一个空格（也包括Tab等空白符），所以\s+表示至少有一个空格，例如匹配' '，' '等；
      \d{3,8}表示3-8个数字，例如'1234567'。

      '010-12345' \d{3}\-\d{3,8}
      
re.match用法
re.match(pattern,string,flasgs=0)
pattern:匹配的正则表达式
string:要匹配的字符串
flags:标志位，控制表达式匹配方式
re.I 忽略大小写
re.L 表示特殊字符集 \w, \W, \b, \B, \s, \S 依赖于当前环境
re.M 多行模式
re.S 即为' . '并且包括换行符在内的任意字符（' . '不包括换行符）
re.U 表示特殊字符集 \w, \W, \b, \B, \d, \D, \s, \S 依赖于 Unicode 字符属性数据库
re.X 为了增加可读性，忽略空格和' # '后面的注释   

match 尝试从字符串的起始位置匹配一个模式,如果不是起始位置匹配成功的话,返回none   
search 全局搜 用法一样 
findall 返回列表 匹配全部相同
'''
re_match1 = re.match("www","wwwbaidu.comwww.asda")
print("匹配的结果：",re_match1)
print("匹配的起点与终点：",re_match1.span())
print("匹配的起点位置：",re_match1.start())
print("匹配的终点位置：",re_match1.end())

re_match2 = re.search(r"href",r'<a href="/du/106/106061/24918201.html" target="_blank">第三百六十二章 仗剑杀之而已</a>')
# print("匹配的整句话：",re_match2.group(0))
# print("匹配的第一个结果：",re_match2.group(1))
# print("匹配的第二个结果：",re_match2.group(2))
print("匹配的结果列表1111111：",re_match2.group())

print(re.findall("AA","aaAAAAAA.cowm",re.I))
print(re.findall("[0-9]+","1234QWEOJLASDLASNDQNWKlkqwjen,n,mas5678"))
re_match3 = re.findall(r"are(.*?),","qweqw qeq hahaha are dashabi lullulu, hahahahhahaha")
print("匹配的整句话：",re_match3)

'''
切分字符串
'''
print("\n切分字符串")
print('a b   c'.split(' '))
print(re.split(r'\s+', 'a         b     c'))
print(re.split(r'[\s\,]+', 'a,b, c  d'))
print(re.split(r'[\s\,\;]+', 'a,b;; c  d'))

'''
分组
'''
print("\n分组")
print(re.match(r'^(\d{3})-(\d{3,8})$', '010-12345'))
print(re.match(r'^(\d{3})-(\d{3,8})$', '010-12345').groups())
print(re.match(r'^(\d{3})-(\d{3,8})$', '010-12345').group(0))
print(re.match(r'^(\d{3})-(\d{3,8})$', '010-12345').group(1))
print(re.match(r'^(\d{3})-(\d{3,8})$', '010-12345').group(2))

'''
贪婪匹配 == 正则匹配默认是贪婪匹配，也就是匹配尽可能多的字符。

由于\d+采用贪婪匹配，直接把后面的0全部匹配了，结果0*只能匹配空字符串了。
必须让\d+采用非贪婪匹配（也就是尽可能少匹配），才能把后面的0匹配出来，加个?就可以让\d+采用非贪婪匹配：
'''
print("\n贪婪匹配")
print(re.match(r'^(\d+)(0*)$', '102300').groups())
print(re.match(r'^(\d+?)(0*)$', '102300').groups())

'''
预编译 生成Regular Expression对象
'''
print("\n预编译")
re_telephone = re.compile(r'^(\d{3})-(\d{3,8})$')
print(re_telephone.match('010-12345').groups())
print(re_telephone.match('010-8086').groups())

'''
邮箱正则表达式
'''
print("\n邮箱正则表达式")

def is_valid_email(emile_str):
    re_emile = re.compile(r'^[0-9a-zA-Z\;]+@[0-9a-zA-Z\;]+\.com', flags=0)
    if re_emile.findall(emile_str):
        print(re_emile.findall(emile_str))
        return True
    else:
        return False

print(is_valid_email("som1a1;1eone@gma;il.com"))