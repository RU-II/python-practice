import tkinter as tk
import tkinter.filedialog as fd
import PIL.Image
import PIL.ImageTk


def dispPhoto(path):
    # 画像を読み込み、モザイクに変換
    newImage = PIL.Image.open(path).convert("L").resize(
        (32, 32)).resize((300, 300), resample=0)
    # そのイメージをラベルに表示する
    imageData = PIL.ImageTk.PhotoImage(newImage)
    imageLabel.configure(image=imageData)
    imageLabel.image = imageData


def openFile():
    fpath = fd.askopenfilename()

    if fpath:
        dispPhoto(fpath)


# ウィンドウ作成
root = tk.Tk()
root.geometry("600x300")  # xはローマ字エックスの小文字  横x縦
# ラベルとボタン作成
btn = tk.Button(text="ファイルを開く", command=openFile)
imageLabel = tk.Label()
# 部品配置 packの命令順に配置される
btn.pack()
imageLabel.pack()
# メインループ　作成画面が動き始める
tk.mainloop()
