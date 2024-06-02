#turtle5kadai.py
#正方形を描く
from turtle import * #タートルグラフィックスを使う準備
shape("turtle")#カメの登場
col = ["orange","limegreen","gold","plum","tomato"]
for i in range(5):
    color(col[i])
    circle(90)
    left(50)
    
done()#おしまい
