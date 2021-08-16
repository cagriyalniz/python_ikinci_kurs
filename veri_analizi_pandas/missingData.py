import pandas as pd

#isnull/dropna/fillna
url = "http://bit.ly/uforeports"

dataUfo = pd.read_csv(url)
print(dataUfo.columns)
print(dataUfo[['City', 'Time']].head(5))

print(dataUfo.isnull().head(5))

print(dataUfo.isnull().sum())

print(dataUfo[dataUfo.City.isnull()])
print(dataUfo[dataUfo.City.isnull()][['State', 'Time']])

dataUfoDropNull = dataUfo.dropna()
print(dataUfo.shape)
print(dataUfoDropNull.shape)
silinenVeriSayisi = dataUfo.shape[0] - dataUfoDropNull.shape[0]
print("silinen veri sayisi {}".format(silinenVeriSayisi))

def TxtYaz():
    temizlenmisUfoFileAp = open("temizlenmisUfoFile.txt", "a")
    temizlenmisUfoFileAp.write(str(dataUfoDropNull))

def CsvYaz():
    temizlenmisUfoFileApCsv = open("temizlenmisUfoFile.csv", "a")
    temizlenmisUfoFileApCsv.write(str(dataUfoDropNull))

# iki fonksiyonda da dosyalarin icine verilerin hepsini yazmiyor. ilk bastakileri yaziyor, arada ....... yazip sondakileri yaziyor

#any sayesinde herhangi bir yerinde bosluk olanlari bulduk
print(dataUfo.dropna(how="any"))

#all sayesinde tüm satiri bosluk olanlari bulduk
print(dataUfo.dropna(how="all"))

print(dataUfo.dropna(subset=['City', 'Colors Reported'], how="all"))

print(dataUfo['Shape Reported'].value_counts(dropna=True))
print(dataUfo['Shape Reported'].value_counts(dropna=False))

dataUfo['Shape Reported'].fillna(value='TANIMLANAMAYAN', inplace=True) #inplace : bellekte degisiklik yapilsin mi
print(dataUfo['Shape Reported'].value_counts(dropna=True))