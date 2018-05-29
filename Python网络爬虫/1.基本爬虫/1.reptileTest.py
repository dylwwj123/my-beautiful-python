import requests, random, os
from bs4 import BeautifulSoup

def getResponse(url, pathUrl):

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
        print("文本编码: ", str_response.encoding)

        soup = BeautifulSoup(str_response.text, "lxml")

        title = soup.find("h1", class_= "post-title").a.text.strip()

        # with open(pathUrl,"w")as f:
        #     f.write(soup.decode("utf-8"))

        return "%s\n\n%s" %(soup,title)

    except requests.exceptions.Timeout:

        return "请求超时"


def postResponse(url):

    agnet_list = [
        "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_5_6; en-US) AppleWebKit/530.9 (KHTML, like Gecko) Chrome/ Safari/530.9",
        "Mozilla/5.0 (iPhone; CPU iPhone OS 5_0_1 like Mac OS X) AppleWebKit/534.46 (KHTML, like Gecko) Mobile/9A405 Safari/7534.48.3",
        "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/535.2 (KHTML, like Gecko) Chrome/15.0.874.120 Safari/535.2",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13; rv:59.0) Gecko/20100101 Firefox/59.0"
    ]

    headers = {
        "User-Agent": random.choice(agnet_list)
    }

    params = {
        "key1" : "value1",
        "key2" : "value2"
    }

    str_response =  requests.post(url, params, headers=headers)
    print("状态码: ",str_response.status_code)
    print("文本编码: ",str_response.encoding)
    print(str_response.text)


pathUrl = "%s%s" %(os.path.abspath('.'),"/2.reptileHTML.html")
reptileUrl = "http://www.santostang.com"
print("get **************")
print(getResponse(reptileUrl, pathUrl))

print("post **************")
postResponse("http://httpbin.org/post")
