import os
import re
from bs4 import BeautifulSoup

pathUrl = "%s%s" %(os.path.abspath('.'),"/5.本地bs4.html")
print(pathUrl)

htmlstr = ""
with open(pathUrl, "r") as f:
    htmlstr = f.read()

soup = BeautifulSoup(htmlstr,"lxml")
#打印文档树格式
# print (soup.prettify())

'''
    Tag 就是 HTML 中的一个个标签
'''
print("\n********************Tag************************")

print("\n", soup.title)

print("\n", soup.head)

print("\n", soup.a)

print("\n", soup.p)

# 对于 Tag，它有两个重要的属性
# name
# soup 对象本身比较特殊，它的 name 即为 [document]，对于其他内部标签，输出的值便为标签本身的名称。
print("\n", soup.name)
print("\n", soup.head.name)

# attrs 字典
print("\n", soup.p.attrs)
print("\n", soup.p['name'])

# NavigableString 获取标签内部的文字
print("\n", soup.a.string)


'''
    遍历文档树
'''

print("\n********************遍历文档树************************")

# (1)直接子节点
print ("\n 直接子节点")

# tag 的 .content 属性可以将tag的子节点以列表的方式输出
print ("\n", soup.head.contents)
print ("\n", soup.head.contents[0])

# tag 的 .children 它返回的不是一个 list，不过我们可以通过遍历获取所有子节点。
print ("\n", soup.head.children)
for childstr in  soup.head.children:
    print (childstr)

# (2)所有子孙节点
# .descendants 和 children类似，我们也需要遍历获取其中的内容。
print ("\n 所有子孙节点 \n")
for childstr in soup.descendants:
    print (childstr)

# (3)多个内容
# stripped_strings
print ("\n 多个内容 \n")
for string in soup.stripped_strings:
    print(repr(string))

# (4)父节点
# .parent 属性
print ("\n 父节点")

print ("\n", soup.p.parent.name, "\n")

content = soup.a.parent
for parent in  content.parents:
    print (parent.name)


'''
    搜索文档树
'''
'''
find_all( name , attrs , recursive , text , **kwargs )

find_all() 方法搜索当前tag的所有tag子节点,并判断是否符合过滤器的条件

name 参数可以查找所有名字为 name 的tag,字符串对象会被自动忽略掉
'''

print("\n******************* find_all *************************")

# 传字符串
print("\n", soup.find_all('b'),"\n")

# 传正则
for tag in soup.find_all(re.compile("^b")):
    print(tag.name)

# 传list
print("\n",soup.find_all(["a", "b"]))

# 传True 可以匹配任何值,下面代码查找到所有的tag,但是不会返回字符串节点
print("\n")
for tag in soup.find_all(True):
    print(tag.name)
print("\n")

# keyword 如果一个指定名字的参数不是搜索内置的参数名,搜索时会把该参数当作指定名字tag的属性来搜索,如果包含一个名字为 id 的参数,Beautiful Soup会搜索每个tag的”id”属性
print(soup.find_all(id='link2'))

#如果传入 href 参数,Beautiful Soup会搜索每个tag的”href”属性
print(soup.find_all(href=re.compile("elsie")))

print("1111111111111")
#使用多个指定名字的参数可以同时过滤tag的多个属性
print(soup.find_all(href=re.compile("elsie"), id='link1'))

#在这里我们想用 class 过滤，不过 class 是 python 的关键词，这怎么办？加个下划线就可以
print(soup.find_all(class_='sister'))

#通过 text 参数可以搜搜文档中的字符串内容.与 name 参数的可选值一样, text 参数接受 字符串 , 正则表达式 , 列表, True
print(soup.find_all(text="EEE"))
print(soup.find_all(text=["Tillie", "EEE", "Lacie"]))
print(soup.find_all(text=re.compile("Dormouse")))

#limit 参数
#find_all() 方法返回全部的搜索结构,如果文档树很大那么搜索会很慢.如果我们不需要全部结果,
#可以使用 limit 参数限制返回结果的数量.效果与SQL中的limit关键字类似,当搜索到的结果数量达到 limit 的限制时,就停止搜索返回结果.
print(soup.find_all("a", limit=1))

#调用tag的 find_all() 方法时,Beautiful Soup会检索当前tag的所有子孙节点,如果只想搜索tag的直接子节点,可以使用参数 recursive=False .

