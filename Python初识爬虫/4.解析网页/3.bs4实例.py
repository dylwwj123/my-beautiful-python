import requests, random, re
from bs4 import BeautifulSoup

'''
BeautifulSoup 可以从HTML或XML中提取数据。
'''

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

    try:
        str_response = requests.get(url, headers=headers, timeout=1)
        print("状态码: ", str_response.status_code)

        #将网页相应体的字符串转换为BeautifulSoup对象。
        soup = BeautifulSoup(str_response.text, "lxml")
        print(soup.prettify()) #html文档树形式输出
        # print(soup.find_all(class_="volume"))


        # for rangeStr in soup.find_all(class_ = "volume"):
        #     for dt in rangeStr.find_all_next("li"):
        #         print(dt)


    except requests.exceptions.Timeout:

        print("请求超时")


# reptileUrl = "https://book.qidian.com/info/1011978632#Catalog"
# getResponse(reptileUrl)


# dic = ""
# for i in 10:
#     print(i)

a = [1,2,3]
b = [4,5,6]
print(dict(zip(a,b)))