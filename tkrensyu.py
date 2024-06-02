#GUIで動くアプリを作ってみるよ

import tkinter as tk #まずこの行を書く必要があるよ

root = tk.Tk() #初めのおまじない

root.geometry("700x500")#ィンドウのサイズを決める
root.title("アプリ練習")#ウィンドウのタイトルを決める
lbl = tk.Label(text="Hello world")#いつもの
lbl = tk.Label(text="初めてのGUIアプリ")#いつもの
lbl.pack() #lblを配置させる必要があるよ





root.mainloop() #終わりのおまじない
