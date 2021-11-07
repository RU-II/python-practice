import pandas as pd
import folium

# データフレームを読み込む
df = pd.read_csv("PythonSecondGrader/200.csv", encoding="shift-jis")
'''
print(len(df))
print(df.columns.values)
'''

# 消火栓のある地点（緯度、経度）をリスト化する
hydraft = df[["緯度", "経度"]].values
print(len(hydraft))
print(hydraft)
'''
# 地図を作って書き出す
m = folium.Map(location=[35.942957, 136.198863], zoom_start=16)  # 地図作成
m.save("PythonSecondGrader/sabae.html")  # html保存
folium.Marker([35.942957, 136.198863]).add_to(m)  # マーカーを追加
m.save("PythonSecondGrader/megane.html")
'''
# 地図を作って書き出す
m = folium.Map(location=[35.942957, 136.198863], zoom_start=16)  # 地図作成
for data in hydraft:
    folium.Marker([data[0], data[1]]).add_to(m)  # マーカーを追加
m.save('PythonSecondGrader/hydraft.html')  # html保存
