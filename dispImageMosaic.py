#s24025
#モザイク画像に変換
#dispImageMosaic.py

import tkinter as tk
import tkinter.filedialog as fd
import PIL.Image
import PIL.ImageTk

def dispPhoto(path):
    #画像を読み込んでモザイクに変換
    newImage=PIL.Image.open(path).convert("L").resize((5,5)).resize((300,300))
    imageData=PIL.ImageTk.PhotoImage(newImage)
    imageLabel.configure(image=imageData)
    imageLabel.image=imageData

def openFile():
    fpath=fd.askopenfilename()
    if fpath:
        dispPhoto(fpath)
        print(fpath)
        lbl2=tk.Label(text=fpath,font=("Helvetica",5))
        lbl2.pack()
root =tk.Tk()
root.geometry("400x350")

lbl=tk.Label(text="画像表示アプリバージョン2.0",font=("Helvetica",20))

btn=tk.Button(text="ファイルを開く",command=openFile)
imageLabel=tk.Label()
btn.pack()
imageLabel.pack()
lbl.pack()

tk.mainloop()
