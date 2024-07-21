# s24025
# Flask_rensyu2.py
# 「こんにちは世界」と書かれたhtml文章を表示するプログラム

# 事前にFlaskモジュールをインストールすると使える
# render__templatはhtmlファイルを扱う際に必要
from flask import Flask, render_template 


#Flaskライブラリをインスタンス化し、app変数に割り当て
# その際、コンストラクタへの引数は実行中のモジュールを指定する
app = Flask(__name__)

# ルートURLに対するリクエストを処理する関数を定義するデコレーター
# 引数にルート'/'を指定するとアクセスした際index()関数が呼び出される
@app.route('/')
def index():
    #templates/index.htmlをあらかじめ作成しておく
    return render_template('index.html')

@app.route('/himitsu')
def index2():
    return render_template('himitsu.html')

if __name__ == '__main__':
    # それぞれのユニークなiPアドレスでアクセスするように設定
    app.run(port=5000, debug=True)

# python flask_rensyu2.pyで実行し
# ブラウザから表示させてみましょう
