import requests
import json
from pprint import pprint
'''
ans = "今日か{key1}です。明日は{key2}です。"
print(ans)

ans = ans.format(key1="晴れ", key2="曇り")
print(ans)
'''

'''
# 現在の天気を取得:都市名
cityname = "Niigata,JP"
url = "http://api.openweathermap.org/data/2.5/weather?q={cityname}&appid={APIkey}&lang=ja&units=metric"
url = url.format(cityname=cityname,
                 APIkey="1d72e3eff33467bf9cb6f0ffc62eaf07")
'''
# 現在の天気を取得:郵便番号
zipcode = "160-0006,JP"
url = "http://api.openweathermap.org/data/2.5/weather?zip={zipcode}&appid={APIkey}&lang=ja&units=metric"
url = url.format(zipcode=zipcode,
                 APIkey="#")
jsondata = requests.get(url).json()

# print(jsondata)
# * 整形して表示
# pprint(jsondata)
print("都市名   = ", jsondata["name"])
print("気温     = ", jsondata["main"]["temp"])
print("天気     = ", jsondata["weather"][0]["main"])
print("天気詳細 = ", jsondata["weather"][0]["description"])

'''
with open("PythonSecondGrader/test2.json", mode="r") as f:
    jsondata = json.loads(f.read())
    # pprint(jsondata)
    print("1つ目のオブジェクト = ", jsondata[0])
    print("都市名 = ", jsondata[0]["name"])
    print("緯度   = ", jsondata[0]["coord"]["lat"])
    print("経度   = ", jsondata[0]["coord"]["lon"])
'''
