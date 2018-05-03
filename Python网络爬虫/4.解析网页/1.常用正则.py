import re

r'''
      .  匹配任意字符                    *  匹配前一个字符0次或多次       + 匹配前一个字符一次或多次
      ?  匹配前一个字符0次或1次           ^  匹配字符串开头              $ 匹配字符串末位
      () 匹配括号内的表达式，也表示一个组   \s 匹配空白字符               \S 匹配非空白字符
      \d 匹配数字 等于[0-9]              \D 匹配任何非数字 等于[^0-9]   \w 匹配字母数字 等于[A-Za-z0-9_]
      \W 匹配非字母数字等于[^A-Za-z0-9_]  [] 表示一组字符
      
re.match用法
re.match(pattern,string,flasgs=0)
pattern:匹配的正则表达式
strig:要匹配的字符串
flags:标志位，控制表达式匹配方式
re.I :忽略大小写     re.L :本地化识别     re.M :多行匹配       re.X :使我们灵活理解正则
re.S :使.匹配包括换行符在内的有所字符      re.U :根据unicode字符集解析字符 影响\w \W \b \B    

match 尝试从字符串的起始位置匹配一个模式,如果不是起始位置匹配成功的话,返回none   
search 全局搜 用法一样 
findall 返回列表 匹配全部相同
'''
re_match1 = re.match("www","wwwbaidu.comwww.asda")
print("匹配的结果：",re_match1)
print("匹配的起点与终点：",re_match1.span())
print("匹配的起点位置：",re_match1.start())
print("匹配的终点位置：",re_match1.end())

re_match2 = re.search(r"(.*)are(.*?),","qweqw qeq hahaha are dashabi lullulu, hahahahhahaha")
print("匹配的整句话：",re_match2.group(0))
print("匹配的第一个结果：",re_match2.group(1))
print("匹配的第二个结果：",re_match2.group(2))
print("匹配的结果列表：",re_match2.group())

print(re.findall("AA","aaAAAAAA.cowm",re.I))
print(re.findall("[0-9]+","1234QWEOJLASDLASNDQNWKlkqwjen,n,mas5678"))
re_match3 = re.findall(r"are(.*?),","qweqw qeq hahaha are dashabi lullulu, hahahahhahaha")
print("匹配的整句话：",re_match3)
