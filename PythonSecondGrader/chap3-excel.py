import pandas as pd
import openpyxl

# * 東アジアで使われている文字幅で表示 https://www.haya-programming.com/entry/2020/04/10/060532
pd.set_option('display.unicode.east_asian_width', True)

# CSVファイルを読み込む
df = pd.read_csv("PythonSecondGrader/test.csv")

# ソート（国語の点数が高いもの順）
kokugo = df.sort_values("国語", ascending=False)
'''
kokugo.to_excel("PythonSecondGrader/csv_to_excel1.xlsx")

# Excelファイルに出力する index=False sheet_name="国語でソート"
kokugo.to_excel("PythonSecondGrader/csv_to_excel2.xlsx",
                index=False, sheet_name="国語でソート")

# 1つのExcelファイルに複数のシートを出力する
with pd.ExcelWriter("PythonSecondGrader/csv_to_excel3.xlsx") as writer:
    df.to_excel(writer, index=False, sheet_name="元のデータ")
    kokugo.to_excel(writer, index=False, sheet_name="国語でソート")
'''
# Excelファイルを読み込む シート1枚目のみ
df = pd.read_excel("PythonSecondGrader/csv_to_excel2.xlsx")
print(df)
# シート名指定
df = pd.read_excel("PythonSecondGrader/csv_to_excel3.xlsx",
                   sheet_name="国語でソート")
print(df)
