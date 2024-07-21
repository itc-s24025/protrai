import sklearn.datasets
import sklearn.svm
import PIL.Image
import numpy
def imageToData (filename):#画像ファイルを数値リストに変換する
    grayImage = PIL.Image.open (filename) .convert ("L")
    grayImage = grayImage.resize ( (8, 8), PIL.Image.Resampling.LANCZOS)
    numImage = numpy.asarray (grayImage, dtype = float)
    numImage = 16-numpy.floor (17*numImage/256)
    numImage = numImage.flatten()
    print(numImage)
    return numImage
def predictDigits (data) :#数値を予測する
    digits = sklearn.datasets.load_digits()
    clf = sklearn.svm.SVC (gamma=0.001)
    clf.fit (digits.data,digits.target)
    n = clf.predict ([data])
    print("予測=",n)
data = imageToData ("tmp/2.png")#パスを確認する
predictDigits (data)
