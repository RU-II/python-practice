import pandas as pd
import matplotlib.pyplot as plt
import japanize_matplotlib

# データフレーム読み込み
df1 = pd.read_csv(
    "PythonSecondGrader/Preview_20211031180311.csv", index_col="時点")
df2 = pd.read_csv(
    "PythonSecondGrader/Preview_20211031180333.csv", index_col="時点")
df3 = pd.read_csv(
    "PythonSecondGrader/Preview_20211031180347.csv", index_col="時点")
'''
print(df1.columns.values)
print(df2.columns.values)
print(df3.columns.values)

# 平均気温で折れ線グラフを表示
df1["年平均気温【℃】"].plot()
plt.ylim(-10, 40)
plt.show()
'''
# 3つのグラフを重ねて表示
df1["年平均気温【℃】"].plot()
df2["最高気温（日最高気温の月平均の最高値）【℃】"].plot()
df3["最低気温（日最低気温の月平均の最低値）【℃】"].plot()
plt.ylim(-10, 40)
plt.legend(loc="lower right")
plt.show()
