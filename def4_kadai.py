#s24025
#main関数練習プログラミング

import random

#ランダムでkujiの中の一つを返す関数
def omikuji():
    kuji=["大吉","中吉","小吉","吉"]
    return random.choice(kuji)

#エントリーポイントの定義
def main():
    kekka = omikuji()
    print("結果は", kekka ,"です。")

if __name__=="__main__":
    main()
