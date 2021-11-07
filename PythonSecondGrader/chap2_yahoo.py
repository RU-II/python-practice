import requests
from bs4 import BeautifulSoup

# Webページを取得して解析する
load_url = "https://news.yahoo.co.jp/categories/it"
html = requests.get(load_url)
soup = BeautifulSoup(html.content, "html.parser")

# classで検索し、その中のすべてのaタグを検索して表示する
# aタグはURLリンクのタグ、Webページでは各トピックス名でもありリンクでもある
topic = soup.find(class_="sc-kDgGX jXOTOw")

for element in topic.find_all("a"):
    print(element.text)
