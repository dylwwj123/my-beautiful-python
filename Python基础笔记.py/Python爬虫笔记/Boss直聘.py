import urllib.request
import ssl
import random
import re

Agnet_list = [
    "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_5_6; en-US) AppleWebKit/530.9 (KHTML, like Gecko) Chrome/ Safari/530.9",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 5_0_1 like Mac OS X) AppleWebKit/534.46 (KHTML, like Gecko) Mobile/9A405 Safari/7534.48.3",
    "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/535.2 (KHTML, like Gecko) Chrome/15.0.874.120 Safari/535.2",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13; rv:59.0) Gecko/20100101 Firefox/59.0"
]

def  choushiCrawler(url):

    headers = {
        "User-Agent" : random.choice(Agnet_list)
    }

    contextssl = ssl._create_unverified_context()

    req = urllib.request.Request(url,headers=headers)

    response = urllib.request.urlopen(req, timeout=10, context=contextssl)

    data = response.read()

    # rechoushi = re.compile('<div class="job-title">(.*?)</div>')
    # relist = rechoushi.findall(data)

    with open(r"/Users/wukaihao/Desktop/python/hello.py/测试的file/coinmeet.html","wb") as f:
        f.write(data)

    print(data)

    # dic = {}
    # arr = []
    # for div in relist:
    #
    #     dic_div = {}
    #
    #     re_u = re.compile('<div class="job-primary">(.*?)</div>')
    #     username = re_u.findall(div)
    #
    #     re_d = re.compile(r'<div class="content">\n<span>(.*?)</span>')
    #     duanzi = re_d.findall(div)
    #
    #     dic_div["workName"] = username
    #     dic_div["duanzi"] = duanzi
    #
    #     arr.append(dic_div)
    #
    # dic["infolist"] = arr
    #
    # return dic

info = choushiCrawler("https://coinmeet.io/")
print(info)