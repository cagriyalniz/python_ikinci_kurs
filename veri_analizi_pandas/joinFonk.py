import pandas as pd
#join/concat
musteriler = {'musteri id' : [1,2,3,4,5],
            'musteri adi': ["ali", "riza", "ahmet", "fikret", "ayhan"],}

faturalar = {'musteri id' : [1,1,2,3,4,4,5],
            'fatura miktari' : [100, 50, 75, 120, 20, 60, 70]}

musterilerDf = pd.DataFrame(musteriler)
faturalarDf = pd.DataFrame(faturalar)

print(pd.merge(musterilerDf, faturalarDf,on='musteri id', how='inner'))

fizikDersi = {'ogrenci no' : [1,2,3,4,5],
            'ogrenci adi': ["ali", "riza", "ahmet", "fikret", "ayhan"],
            'fizik ders notu' : [100, 50, 75, 70, 20]}

matematikDersi = {'ogrenci no' : [1,2,6,8],
            'ogrenci adi': ["ali", "riza", "kamil", "fatma"],
            'matematik ders notu' : [95, 75, 75, 80]}

fizikDersiDf = pd.DataFrame(fizikDersi)
matematikDersiDf = pd.DataFrame(matematikDersi)
print(pd.merge(fizikDersiDf, matematikDersiDf, on='ogrenci no', how='left'))

print(pd.concat([fizikDersiDf, matematikDersiDf]))

print(pd.concat([fizikDersiDf, matematikDersiDf], axis=1)) #yan yane concat etmeyi saglar