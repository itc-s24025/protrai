#s24025
#関数で消費税を計算するプログラム
#消費税プログラム

def postTaxPrice(price):
    ans=price*1.1
    return ans

print(postTaxPrice(120),"円")
print(postTaxPrice(128),"円")
print(postTaxPrice(980),"円")
