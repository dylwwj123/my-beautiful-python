import urllib.request
import random

url = "http://www.baidu.com"

#添加多个模拟浏览器
Agnet_list = [
    "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_5_6; en-US) AppleWebKit/530.9 (KHTML, like Gecko) Chrome/ Safari/530.9",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 5_0_1 like Mac OS X) AppleWebKit/534.46 (KHTML, like Gecko) Mobile/9A405 Safari/7534.48.3",
    "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/535.2 (KHTML, like Gecko) Chrome/15.0.874.120 Safari/535.2",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13; rv:59.0) Gecko/20100101 Firefox/59.0"
]

#随机获取一个模拟浏览器
agents_str = random.choice(Agnet_list)

#模拟请求头
custom_headers = {
    "User-Agent":agents_str
}

#设置一个请求体
req = urllib.request.Request(url,headers=custom_headers)

#发起请求
response = urllib.request.urlopen(req)
data = response.read()
print(data)

#将爬取到的网页写入文件
with open(r"/Users/wukaihao/Desktop/python/hello.py/测试的file/模拟浏览器爬虫.html","wb") as f:
    f.write(data)