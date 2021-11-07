import pandas as pd

# * 東アジアで使われている文字幅で表示 https://www.haya-programming.com/entry/2020/04/10/060532
pd.set_option('display.unicode.east_asian_width', True)

# データフレームを読み込む
df = pd.read_csv("PythonSecondGrader/13TOKYO.csv",
                 header=None, encoding="shift_jis")
print(len(df))
print(df.columns.values)

# 「２」の列が「1600006」の住所を抽出して表示
results = df[df[2] == 1600006]
print(results[[2, 6, 7, 8]])

# 「8」の列が「四谷」の住所を抽出して表示
results = df[df[8] == "四谷"]
print(results[[2, 6, 7, 8]])

# 「8」の列に「四谷の文字が含まれる住所を抽出して表示」
results = df[df[8].str.contains("四谷")]
print(results[[2, 6, 7, 8]])
