import urllib.request
import ssl
import random
import re
import os

Agnet_list = [
    "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_5_6; en-US) AppleWebKit/530.9 (KHTML, like Gecko) Chrome/ Safari/530.9",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 5_0_1 like Mac OS X) AppleWebKit/534.46 (KHTML, like Gecko) Mobile/9A405 Safari/7534.48.3",
    "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/535.2 (KHTML, like Gecko) Chrome/15.0.874.120 Safari/535.2",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13; rv:59.0) Gecko/20100101 Firefox/59.0"
]

def  imageCrawler(url, topath):

    headers = {
        "User-Agent" : random.choice(Agnet_list)
    }

    contextssl = ssl._create_unverified_context()

    req = urllib.request.Request(url,headers=headers)

    response = urllib.request.urlopen(req, timeout=10, context=contextssl)

    data = response.read().decode("utf-8")

    re_index = '<div style="position: relative">\n<img src="//(.*?)"'
    re_image = re.compile(re_index, re.S)
    re_list = re_image.findall(data)

    num = 1
    for imgurl in re_list:
        path = os.path.join(topath, str(num)+".jpg")
        num += 1
        urllib.request.urlretrieve("http://"+imgurl,filename=path)

imageCrawler("https://search.yhd.com/c9719-0-0", "/Users/wukaihao/Desktop/python/hello.py/测试的file/爬取image")