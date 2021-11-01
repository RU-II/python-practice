import pandas as pd
import matplotlib.pyplot as plt
import japanize_matplotlib

# データフレームを読み込む インデックスに使う列を"全国・都道府県"に
df = pd.read_csv("PythonSecondGrader/FEH_00200524_211031170355.csv",
                 index_col="全国・都道府県", encoding="shift_jis")
print(len(df))
print(df.columns.values)
'''
# 2019年の列データで人口の多い順の棒グラフを作って表示する
df = df.drop("全国", axis=0)  # 全国の行を削除
df["2019年"] = pd.to_numeric(df["2019年"].str.replace(",", ""))  # * カンマを削除
print(df["2019年"])
df = df.sort_values("2019年", ascending=False)  # 降順に並び替え
df["2019年"].plot.bar(figsize=(10, 6))  # figsize(幅インチ, 高さインチ)
plt.show()
'''
# 2019年と2018年の列データの差の棒グラフを作って表示する
df = df.drop("全国", axis=0)  # 全国の行を削除
df["2018年"] = pd.to_numeric(df["2018年"].str.replace(",", ""))  # * カンマを削除
df["2019年"] = pd.to_numeric(df["2019年"].str.replace(",", ""))  # * カンマを削除
df["人口増減"] = df["2019年"] - df["2018年"]
df = df.sort_values("人口増減", ascending=False)  # 降順に並び替え
df["人口増減"].plot.bar(figsize=(10, 6))  # figsize(幅インチ, 高さインチ)
plt.ylim(-40, 14000)  # 縦軸のスケールを設定
plt.show()
print(df["人口増減"].loc["新潟県"])
