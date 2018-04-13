import urllib.request #导入爬虫库。

url = urllib.request.urlopen("http://www.baidu.com/") #向指定地址发起的请求,并返回服务器响应的数据。

# res = url.read() #读取文件的全部内容,会把读取到的数据赋值给一个字符串变量。
# res = url.read().decode("utf-8") #utf-8编码过文件的数据。
# res = url.readline() #读取一行数据。
# res = url.readlines() #读取文件的全部内容,会把读取到的数据赋值给一个列表变量。

# print(res)

#将爬取到的网页写入文件
# with open(r"/Users/wukaihao/Desktop/python/hello.py/file/简单爬虫.html","wb") as f:
#     f.write(res)