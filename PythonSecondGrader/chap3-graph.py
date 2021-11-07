import pandas as pd
import matplotlib.pyplot as plt
import japanize_matplotlib

# CSVファイルを読み込む(名前の列をインデックスで)
df = pd.read_csv("PythonSecondGrader/test.csv", index_col=0)
'''
print(df)

# グラフを作って表示する
df.plot()  # * pandas内部からmatplotlibの昨日を呼び出して利用している
plt.show()

# 棒グラフを作って表示する
df.plot.bar()
plt.legend(loc="lower right")
plt.show()

# 棒グラフ(水平)を作って表示する
df.plot.barh()
plt.legend(loc="lower left")
plt.show()

# 積み上げ棒グラフを作って表示する
df.plot.bar(stacked=True)
plt.legend(loc="lower right")
plt.show()

# 箱ひげグラフを作って表示する
df.plot.box()
plt.show()

# 面グラフを作って表示する
df.plot.area()
plt.legend(loc="lower right")
plt.show()

# 国語の棒グラフを作って表示する
df["国語"].plot.bar()
plt.legend(loc="lower left")
plt.show()

# 国語と数学の棒グラフを作って表示する
df["国語"].plot.barh()
plt.legend(loc="lower left")
plt.show()

# C子の棒グラフを作って表示する
df.loc["C子"].plot.barh()
plt.legend(loc="lower left")
plt.show()

# C子の円グラフを作って表示する
df.loc["C子"].plot.pie(labeldistance=0.6)  # ! labeldistance=中心からの距離
plt.legend(loc="lower left")
plt.show()

# 教科ごとの棒グラフを作って表示する
df.T.plot.bar()
plt.legend(loc="lower right")
plt.show()

# グラフの色を指定
colorlist = ["skyblue", "steelblue", "tomato", "cadetblue", "orange", "sienna"]
df.T.plot.bar(color=colorlist)
plt.legend(loc="lower right")
plt.show()
'''
# 画像ファイル出力
colorlist = ["skyblue", "steelblue", "tomato", "cadetblue", "orange", "sienna"]
df.T.plot.bar(color=colorlist)
plt.legend(loc="lower right")
plt.savefig("PythonSecondGrader/bargraph.png")
