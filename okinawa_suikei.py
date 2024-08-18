#s24025
#沖縄県の推計人口より最新情報をスクレイピングするpythonコード
#https://www.pref.okinawa.jp/toukeika/estimates/estimates_suikei.html
import requests
from bs4 import BeautifulSoup
uri = 'https://www.pref.okinawa.jp/toukeika/estimates/estimates_suikei.html'
html = requests.get(uri)
#文字コードをShift_JISにエンコーディング
html.encoding = 'Shift-JIS'
soup = BeautifulSoup(html.text, 'html.parser')
table = soup.find('table', class_="table1 font2 gyo5")
print(soup.find('title').string)
#tableからtdタグのalignが"right"になっているものを取り出す
a = []
for element in table.find_all('td', align="right"):
    a.append(element.text)
b = []
for elements in table.find_all('td', align="center"):
    b.append(elements.text)
print(f"総人口：{a[0]}")
print(f"男：{a[1]}")
print(f"女：{a[2]}")
