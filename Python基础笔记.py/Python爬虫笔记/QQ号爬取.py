import urllib.request
import ssl
import random
import re
import os

def writeFileByte(htmlBytes,toPath):

    with open(toPath, "wb")as f:
        f.write(htmlBytes)


def writeFileStr(htmlBytes,toPath):

    with open(toPath, "w")as f:
        f.write(htmlBytes.decode("utf-8"))


def getResponse(url):

    Agnet_list = [
        "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_5_6; en-US) AppleWebKit/530.9 (KHTML, like Gecko) Chrome/ Safari/530.9",
        "Mozilla/5.0 (iPhone; CPU iPhone OS 5_0_1 like Mac OS X) AppleWebKit/534.46 (KHTML, like Gecko) Mobile/9A405 Safari/7534.48.3",
        "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/535.2 (KHTML, like Gecko) Chrome/15.0.874.120 Safari/535.2",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13; rv:59.0) Gecko/20100101 Firefox/59.0"
    ]

    headers = {
        "User-Agent": random.choice(Agnet_list)
    }

    contextssl = ssl._create_unverified_context()

    req = urllib.request.Request(url, headers=headers)

    response = urllib.request.urlopen(req, timeout=30, context=contextssl)

    return response.read()


def qqCrawler(url):

    response = getResponse(url)

    #$从判断是不是最尾部
    re_qq = re.compile(r"[1-9]\d{8,9}")

    qq_list = re_qq.findall(response.decode("utf-8"))

    #去重
    qq_list = list(set(qq_list))

    return qq_list


def urlCrawler(url):

    response = getResponse(url)

    re_url = re.compile(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*,]|(?:%[0-9a-fA-F][0-9a-fA-F]))+',re.I)

    url_list = re_url.findall(response.decode("utf-8"))

    url_list = list(set(url_list))

    return url_list


qq_list = qqCrawler(r"https://www.douban.com/group/topic/17359302/?start=0")
# print(qq_list)

url_list = urlCrawler(r"https://www.douban.com/group/topic/17359302/?start=0")
print(url_list)