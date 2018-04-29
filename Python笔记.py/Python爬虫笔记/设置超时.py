import urllib.request

#如果网页长时间未响应，系统判断超时，无法爬取
for i in range(1,101):
    try:
        response = urllib.request.urlopen("http://www.baidu.com/", timeout=0.01)
        print("请求成功")
    except:
        print("请求超时111111111111")