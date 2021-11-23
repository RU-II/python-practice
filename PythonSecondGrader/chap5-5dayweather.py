import requests
import json
from pprint import pprint
from datetime import datetime, timedelta, timezone
import pandas as pd
import matplotlib.pyplot as plt
import japanize_matplotlib

# 5日間（3時間ごと）の天気予報を取得する：東京
APIkey = "#"
url = "http://api.openweathermap.org/data/2.5/forecast?q={cityname}&appid={APIkey}&lang=ja&units=metric"
cityname = "Tokyo,JP"
url = url.format(cityname=cityname, APIkey=APIkey)

jsondata = requests.get(url).json()
# pprint(jsondata)
# * データフレームを作成(項目名：気温)
df = pd.DataFrame(columns=["気温"])
tz = timezone(timedelta(hours=+9), 'JST')
# * dt=タイムスタンプ(日時を数値で表したもの)
# * dt_txt=日時
for dat in jsondata["list"]:
    # * UTCのタイムスタンプからタイムゾーン(JST)での日時を求める
    jst = str(datetime.fromtimestamp(dat["dt"], tz))[:-9]
    # UTCとJSTの日時を表示
    # print("UTC={ust}, JST={jst}".format(ust=dat["dt_txt"], jst=jst))
    weather = dat["weather"][0]["description"]
    temp = dat["main"]["temp"]
    # print("日時:{jst}, 天気:{w},気温:{t}度".format(jst=jst, w=weather, t=temp))
    # * 日時をインデックスにして気温のデータを追加
    df.loc[jst] = temp
# pprint(df)
df.plot(figsize=(15, 8))
plt.ylim(-10, 40)
plt.grid()
plt.show()

'''
# UTC(協定世界時)をJST(日本標準時)に変換
timestamp = 1562889600

tz = timezone(timedelta(), 'UTC')
utc = datetime.fromtimestamp(timestamp, tz)
print(utc)

tz = timezone(timedelta(hours=+9), 'JST')
jst = datetime.fromtimestamp(timestamp, tz)
print(jst)
print(str(jst)[:-9])  # 後ろから9文字削除
'''
