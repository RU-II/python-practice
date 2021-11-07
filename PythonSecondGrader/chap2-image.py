import requests
from pathlib import Path  # フォルダアクセス用ライブラリ

# 保存用フォルダを作る
out_folder = Path("PythonSecondGrader/download")  # ()内階層 今回親はPython
out_folder.mkdir(exist_ok=True)

# 画像ファイルを取得する
image_url = "https://www.ymori.com/books/python2nen/sample1.png"
imgdata = requests.get(image_url)

# URLから最後のファイル名を取り出して、保存フォルダ名とつなげる
filename = image_url.split("/")[-1]
# split ()内で区切る リストの最後の要素指定インデックス番号-1 https://techacademy.jp/magazine/28403
out_path = out_folder.joinpath(filename)

# 画像データを、ファイルに書き出す
with open(filename, mode="wb") as f:
    f.write(imgdata.content)
# 画像データを、フォルダ内のファイルに書き出す
with open(out_path, mode="wb") as f:
    f.write(imgdata.content)
