from numpy import True_
import pandas as pd
from pandas.core.reshape.pivot import pivot_table

filmler = pd.read_csv("imdb-1000.csv")
print(filmler.columns)

#axis = 1 --> kolon // axis = 0 --> satır
print(filmler.drop("content_rating", axis=1).drop("actors_list", axis = 1).columns)

print(filmler.head(4))
print(filmler.drop(1, axis=0).head(4))
print(filmler.drop(1, axis=0).drop(2, axis=0).head(4))

rowToDrop = [0, 1, 2, 3, 4]
print(filmler.drop(rowToDrop, axis=0).head(4)[['title']])


#ilk 100 filmi degisik bir sekilde alma yontemi
sayac = 0
dusenSatirlar = list()

for i in range(100,len(filmler),1):
    dusenSatirlar.insert(sayac, i)
    sayac = sayac + 1

yeniFilmler = filmler.drop(dusenSatirlar, axis=0)
print((yeniFilmler)[['title']])
