import urllib.request
import ssl
import json
import random

Agnet_list = [
    "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_5_6; en-US) AppleWebKit/530.9 (KHTML, like Gecko) Chrome/ Safari/530.9",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 5_0_1 like Mac OS X) AppleWebKit/534.46 (KHTML, like Gecko) Mobile/9A405 Safari/7534.48.3",
    "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/535.2 (KHTML, like Gecko) Chrome/15.0.874.120 Safari/535.2",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13; rv:59.0) Gecko/20100101 Firefox/59.0"
]

def  ajaxCrawler(url):

    headers = {
        "User-Agent": random.choice(Agnet_list)
    }

    req = urllib.request.Request(url,headers=headers)

    contextssl = ssl._create_unverified_context()

    response = urllib.request.urlopen(req, timeout=10, context=contextssl)

    data = response.read().decode("utf-8")

    jsonData = json.loads(data)

    return jsonData


page = 0

for i in range(3):

    info = ajaxCrawler(("https://movie.douban.com/j/chart/top_list?type=11&interval_id=100:90&action=&start=%d&limit=20" %(page)))

    print("------------------\n%s" %(info))

    page += 20


