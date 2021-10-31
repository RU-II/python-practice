import pandas as pd

# ! 東アジアで使われている文字幅で表示 https://www.haya-programming.com/entry/2020/04/10/060532
pd.set_option('display.unicode.east_asian_width', True)

# CSVファイルを読み込む
df = pd.read_csv("PythonSecondGrader/test.csv")  # ()内path
print(df)

# 表データの情報を表示
print("データの件数 = ", len(df))
print("項目名      = ", df.columns.values)
print("インデックス=", df.index.values)

# 1列のデータを表示
print("国語の列データ\n", df["国語"])  # df["列名"]

# 複数の列のデータを表示
print("国語と数字の列データ\n", df[["国語", "数学"]])  # df[["列名1","列名2"]]

# 1行のデータを表示
print("c子のデータ\n", df.loc[2])

# 複数の行のデータを表示
print("c子とD郎のデータ\n", df.loc[[2, 3]])

# 指定した行の指定した列のデータを表示
print("C子の国語データ\n", df.loc[2]["国語"])

# 1列のデータを追加
df["美術"] = [58, 73, 82, 77, 94, 96]
print("列データ(美術)を追加\n", df)

# 1行のデータを追加
df.loc[6] = ["G恵", 90, 92, 94, 96, 92, 98]
print("行データ(G恵)を追加\n", df)

# 「名前」の列を削除
print("「名前」の列を削除\n", df.drop("名前", axis=1))  # ! 列はaxis=1

# インデックス2の行を削除 axis=0
print("インデックス2の行を削除\n", df.drop(2, axis=0))  # ! 行はaxis=0

# 条件に合うデータを抽出する
data_s = df[df["国語"] >= 90]
print("国語が90点以上\n", data_s)

data_c = df[df["数学"] < 70]
print("数学が70点未満\n", data_c)

# 集計(最大値、最小値、平均値、中央値、合計など)をして表示
print("数学の最高点 =", df["数学"].max())
print("数学の最低点 =", df["数学"].min())
print("数学の平均点 =", df["数学"].mean())
print("数学の中央値 =", df["数学"].median())
print("数学の合計 =", df["数学"].sum())
print("行合計 =", df.sum(axis=1))  # ! 行の合計はaxis=1、行指定不明

# ソート(並べ替え)をして表示
kokugo = df.sort_values("国語", ascending=False)
print("国語の点数が高いもので順でソート\n", kokugo)

# 行と列を入れ替える
print("行と列を入れ替える\n", df.T)

# データをリスト化する
print("Pythonのリストデータ化\n", df.values)

# csvファイルに出力する
kokugo.to_csv("PythonSecondGrader/export1.csv")  # ! ()内path

# csvファイルに出力する（インデックスを削除）
kokugo.to_csv("PythonSecondGrader/export2.csv", index=False)

# csvファイルに出力する（インデックスとヘッダーを削除）
kokugo.to_csv("PythonSecondGrader/export3.csv", index=False, header=False)
