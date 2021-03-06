import requests

# Webページを取得する
url = "https://www.ymori.com/books/python2nen/test1.html"
response = requests.get(url)

# 文字化けしないようにする
# response.encoding = response.apparent_encoding
response.encoding = 'utf-8'

# ファイルを書き込みモードで開いて
filename = "PythonSecondGrader/download.txt"  # Pythonからの相対パス
f = open(filename, mode="w")

# ネットから取得した読み込んだデータを書き込んで
f.write(response.text)

# 最後にファイルを閉じる
f.close()
