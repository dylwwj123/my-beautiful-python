import json

jsonstr = r"""
    {"sb":[{"CityId":18,"CityName":"西安","ProvinceId":27,"CityOrder":1},
    {"CityId":53,"CityName":"广州","ProvinceId":27,"CityOrder":1}],
     "2b":[{"ss":"sb"}]}
"""

#将json转为python数据类型的对象
jsonData = json.loads(jsonstr)
print(jsonData)
print(jsonData["sb"])
print(jsonData["2b"])

#将python数据类型的对象转为json
jsonstr2 = r"""
    {"sb":[{"CityId":18,"CityName":"西安","ProvinceId":27,"CityOrder":1}]}
"""
jsonData2 = json.dumps(jsonstr2)
print("1111111111"+jsonData2)
print(type(jsonData2))

#写本地json
jsondic = {"sb":[{"CityId":18,"CityName":"西安","ProvinceId":27,"CityOrder":1},
    {"CityId":53,"CityName":"广州","ProvinceId":27,"CityOrder":1}],
     "2b":[{"ss":"sb"}]}

path0 = r"/Users/wukaihao/Desktop/python/hello.py/测试的file/json2.json"
with open(path0,"w") as f:
    json.dump(jsondic,f)

#读取本地json
with open(path0,"rb") as f:
    data = json.load(f)
    print(data)
