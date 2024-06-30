#s24025 entry_kadai.py
#エントリーウィジットで受けた金額を税込み(10%)価格として出力するプログラムを作成してください
#続きはこのコードをアレンジして各自作成してください

import tkinter as tk #TKINTERをTKと略して

def dispLabel():
    #entryメソッドを使用して入力を受け付け変数aに格納
    a=int(entry.get())
    print(f"aは{type(a)}") #ログの出力
    lbl.config(text=f"税込み価格は{a*1.1}円です。")
    
root=tk.Tk()
root.title("税込み価格出力")
root.geometry("400x200") #画面の大ききを決める

lbl=tk.Label(text="税込み計算します",font=("Helvetica",20))
entry=tk.Entry(font=("Helvetica",20))
btn=tk.Button(text="計算する",font=("Helvetica",20), command=dispLabel)

lbl.pack()
entry.pack()
btn.pack()

tk.mainloop()
