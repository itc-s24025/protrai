#s24025
#おみくじおみくじおみくじ モジュール名「omikuji_tk.py」

import tkinter as tk#まずこの行を書く必要があるよ
import random 
root=tk.Tk()#初めのおまじない

root.geometry("700x500")#ウィンドウのサイズを決める
root.title("アプリ練習")#ウィンドウのタイトルを決める

kuji=["大吉","中吉","小吉","凶"]


lbl = tk.Label(text=(random.choice(kuji)))
lbl.pack() #lblを配置させる必要があるよ

root.mainloop()#終わりのおまじない






