#app2.py バージョン2
import tkinter as tk #tkinterをインポートしてtkとして略して使う

def dispLabel():
    lbl1.config(text="こんにちは")

def dispLabel2():
    lbl2.config(text="えらい")

root = tk.Tk() #画面を作る
root.geometry("400x200") #画面の大きさを決める

lbl1 = tk.Label(text="",font=("Helvetica",10)) #ラベルを作る
btn1 = tk.Button(text="PUSH",command=dispLabel,font=("Helvetica",10)) #ボタンを作る



lbl2 = tk.Label(text="", font=("Helvetica",30))
btn2 = tk.Button(text="何もしないボタン",command=dispLabel2,font=("Helvetica",10))

lbl1.pack() #画面にラベルを配置
btn1.pack() #画面にボタンを配置
lbl2.pack()
btn2.pack()
tk.mainloop() #作ったウィンドウを表示する
