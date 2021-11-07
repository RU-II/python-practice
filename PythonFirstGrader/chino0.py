import tkinter as tk
import tkinter.filedialog as fd
import PIL.Image
import PIL.ImageTk

# 画像ファイルを数値リストに変換する
def imageToData(filename):
    # 画像を8x8のグレースケールに変換
    grayImage = PIL.Image.open(filename).convert("L")
    grayImage = grayImage.resize((8, 8), PIL.Image.ANTIALIAS)
    # その画像を表示する
    dispImage = PIL.ImageTk.PhotoImage(grayImage.resize((300,300)))
    imageLabel.configure(image=dispImage)
    imageLabel.image = dispImage

# ファイルダイアログを開く
def openFile():
    fpath = fd.askopenfilename()
    if fpath:
        # 画像ファイルを数値リストに変換する
        data = imageToData(fpath)

# ウィンドウ作成
root = tk.Tk()
root.geometry("400x400")  # xはローマ字エックスの小文字  横x縦
# ラベルとボタン作成
btn = tk.Button(root, text="ファイルを開く", command=openFile)
imageLabel = tk.Label()
# 部品配置 packの命令順に配置される
btn.pack()
imageLabel.pack()
# メインループ　作成画面が動き始める
tk.mainloop()