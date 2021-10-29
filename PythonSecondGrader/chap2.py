import requests
from bs4 import BeautifulSoup
import urllib

# Webページを取得して解析する
load_url = "https://www.ymori.com/books/python2nen/test2.html"
html = requests.get(load_url)
soup = BeautifulSoup(html.content, "html.parser")

# HTML全体を表示する
print(soup)

# title、h2、liタグを検索して表示する
print(soup.find("title"))
print(soup.find("h2"))
print(soup.find("li"))

# title、h2、liタグを検索して、その文字列を表示する
print(soup.find("title").text)
print(soup.find("h2").text)
print(soup.find("li").text)

# すべてのliタグを検索して、その文字列を表示する
for element in soup.find_all("li"):
    print(element.text)

# IDで検索して、そのタグの中身を表示する
chap2 = soup.find(id="chap2")
print(chap2)

# IDで検索し、その中のすべてのliタグを検索して表示する
chap2 = soup.find(id="chap2")
for element in chap2.find_all("li"):
    print(element.text)

# すべてのaタグを検索して、リンクを表示する
for element in soup.find_all("a"):
    print(element.text)  # aタグのテキストを表示
    url = element.get("href")  # aタグのurlを表示
    print(url)

# すべてのaタグを検索し、リンクを絶対URLで表示する
for element in soup.find_all("a"):
    print(element.text)
    url = element.get("href")
    link_url = urllib.parse.urljoin(load_url, url)
    print(link_url)

# ファイルを書き込みモードで開く
filename = "linklist.txt"
with open(filename, "w") as f:
    # すべてのaタグを検索し、リンクを絶対URLで書き出す
    for element in soup.find_all("a"):
        url = element.get("href")
        link_url = urllib.parse.urljoin(load_url, url)
        f.write(element.text+"\n")
        f.write(link_url+"\n")
        f.write("\n")
