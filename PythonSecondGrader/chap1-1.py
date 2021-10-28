import requests

# Webページを取得する
url = "https://www.ymori.com/books/python2nen/test1.html"
response = requests.get(url)

# 文字化けしないようにする
response.encoding = response.apparent_encoding  # ! 文字化けした
# response.encoding = 'utf-8'  # ! 文字化けした
# *https://adatarag3.blogspot.com/2019/03/pcwindows10utf-8.html 文字化け解決参照

# 取得した文字列データを表示する
print(response.encoding)
print(response.text)
