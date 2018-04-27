import urllib.request
import urllib.parse
import json

"""
进行客户端与服务端消息传递的时候使用 比如：
GET  : 通过URL网址传递信息，可以直接在URL网址上添加要传递的信息
POST : 可以像服务器提交数据，是一种比较流行的，比较安全的数据传递方式
"""

"""
GET  : 把数据拼接到请求路径后面传递给服务器，速度快，不安全
"""
# try:
#     urlget = "http://api.k780.com:88/?app=weather.today&weaid=1&appkey=10003&sign=b59bc3ef6191eb9f747dd4e83c99f2a4&format=json"
#     response = urllib.request.urlopen(urlget, timeout=5)
#     data = response.read().decode("utf-8")
#     jsonData = json.loads(data)
#     print(jsonData)
# except:
#     print("请求超时")

"""
POST  : 把参数进行打包,单独传输，速度慢，数量大，安全 对服务器数据进行修改时使用
"""
urlpost = "http://www.example.com"
dp = {
    "parameter1" : "11",
}
#对发送的数据打包
postData = urllib.parse.urlencode(dp).encode("utf-8")
#请求体
req = urllib.request.Request(urlpost, data=postData)
#请求
responsePost = urllib.request.urlopen(req)

print(responsePost.read().decode("utf-8"))
