import requests, random, re

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
        str_response = requests.get(url, headers=headers, timeout=10)
        print("状态码: ", str_response.status_code)

        if str_response.status_code == 200:
            return str_response.text
        else:
            return "%d 请求失败" %(str_response.status_code)

    except requests.exceptions.Timeout:
        return "请求超时"

reptileUrl = "https://movie.douban.com/chart"

re_findallTitle = re.findall(r'title="(.*?)">',getResponse(reptileUrl), re.S)

re_findallDetileTitle = re.findall(r'<span style="font-size:13px;">(.*?)</span>',getResponse(reptileUrl), re.S)

re_list_findall = []
for rangeIndex in range(len(re_findallDetileTitle)):
    re_str_findall = re_findallTitle[rangeIndex] + r" / %s" %(re_findallDetileTitle[rangeIndex])
    re_list_findall.append(re_str_findall)

print(re_list_findall)