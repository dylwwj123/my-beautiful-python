import urllib.request

#向指定地址发起的请求,并返回服务器响应的数据。
# response = urllib.request.urlopen("http://www.baidu.com")

# res = response.read() #读取文件的全部内容,会把读取到的数据赋值给一个字符串变量。
# res = response.read().decode("utf-8") #utf-8编码过文件的数据。
# res = response.readline() #读取一行数据。
# res = response.readlines() #读取文件的全部内容,会把读取到的数据赋值给一个列表变量。

#response 属性

#返回当前环境的有关信息
# print(response.info())
#返回当前正在爬取的url地址
# print(response.geturl())
#返回状态码
# print(response.getcode())
#200 是请求成功      200以上的一般是请求成功的
#304 是有缓存        300以上的一般是缓存相关的
#404 访问请求失败     400以上的一般是访问出错了
#500 服务器内部错误    500以上的一般是服务器有问题
# if response.getcode() == 200 or response.getcode() == 304:
#     print("请求成功")

# print(res)
# print(type(res))

#将爬取到的网页写入文件1
# with open(r"/Users/wukaihao/Desktop/python/hello.py/测试的file/简单爬虫.html","wb") as f:
#     f.write(res)

# oldurl = r"https://www.baidu.com/s?wd=%E5%95%8A%E5%95%8A%E5%95%8A&rsv_spt=1&rsv_iqid=0x944cb1200001f19f&issp=1&f=8&rsv_bp=0&rsv_idx=2&ie=utf-8&tn=monline_3_dg&rsv_enter=1&rsv_sug3=7&rsv_sug1=4&rsv_sug7=100&rsv_sug2=0&inputT=2528&rsv_sug4=3702"
#
# #解码
# uniurl = urllib.request.unquote(oldurl)
# print(uniurl)
# #编码
# newurl = urllib.request.quote(uniurl)
# print(newurl)

#将爬取到的网页写入文件2
#urlretrieve 在执行的过程中，会产生一些缓存
urllib.request.urlretrieve("http://www.baidu.com",filename=r"/Users/wukaihao/Desktop/python/Python笔记.py/测试的file/简单爬虫2.html")
#清除缓存
urllib.request.urlcleanup()