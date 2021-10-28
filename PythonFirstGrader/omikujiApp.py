import tkinter as tk
import random


def dispLabel():
    kuji = ["大吉", "中吉", "小吉", "凶"]
    lbl.configure(text=random.choice(kuji))

# ウィンドウ作成
root = tk.Tk()
root.geometry("600x300")  # xはローマ字エックスの小文字  横x縦
# ラベルとボタン作成
lbl = tk.Label(text="LABEL")
btn = tk.Button(text="PUSH", command=dispLabel)
# 部品配置 packの命令順に配置される
lbl.pack()
btn.pack()
# メインループ　作成画面が動き始める
tk.mainloop()
