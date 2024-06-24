#s24025
#時計アプリ
#時計アプリはモジュール名「time_kadai.py」で作成します
#時計アプリを使いやすくバージョンアップしていきます

import datetime
import tkinter as tk#GUIでアプリを作ることができるモジュール

#時間を処理する部分を関数で実装
def update_time(): #update_time関数を作成
    now = datetime.datetime.now()
    current_time = now.strftime("%Y年%m月%d日 %H時%M分%S秒") #()内は時間の時間の設定
    #
    lbl.config(text = current_time) #ウィンドウの中身(現在の時刻)を挿入
    root.after(1000, update_time) #自分をもう一回呼び出す意味です
    
#TKuinterのウィンドウを作成
root = tk.Tk() #初めのおまじない

root.title("時計アプリ")
#
lbl = tk.Label()
lbl.config(text = "", font = ("Helvetica",20)) #フォントの種類、サイズ
lbl.pack()

#関数の呼び出し
update_time()


root.mainloop() #終わりのおまじない
