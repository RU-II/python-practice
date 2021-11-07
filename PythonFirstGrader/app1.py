import tkinter as tk

def dispLabel():
    lbl.configure(text="こんにちは")
#ウィンドウ作成
root = tk.Tk()
root.geometry("600x300")  #xはローマ字エックスの小文字  横x縦
#ラベルとボタン作成
lbl = tk.Label(text="LABEL")
btn = tk.Button(text="PUSH", command = dispLabel)
#部品配置 packの命令順に配置される
lbl.pack()
btn.pack()
#メインループ　作成画面が動き始める
tk.mainloop()
