import urllib.request
import ssl
import random
import re
import json

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

    data = response.read().decode("utf-8")

    reindex = r'<div class="author clearfix">(.*?)<span class="stats-vote">'
    rechoushi = re.compile(reindex, re.S)
    relist = rechoushi.findall(data)
    # print(relist)

    dic = {}
    arr = []
    for div in relist:

        dic_div = {}

        re_u = re.compile(r"<h2>(.*?)</h2>", re.S)
        username = re_u.findall(div)

        re_d = re.compile(r'<div class="content">\n<span>(.*?)</span>', re.S)
        duanzi = re_d.findall(div)

        dic_div["username"] = username
        dic_div["duanzi"] = duanzi

        arr.append(dic_div)

    dic["infolist"] = arr

    return dic

info = choushiCrawler("https://www.qiushibaike.com/text/page/1/")
print(info)
# jsonData2 = json.dumps(info)
# print(jsonData2)