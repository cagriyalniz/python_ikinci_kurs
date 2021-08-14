import pandas as pd
import numpy as np
from pandas.core import indexing
#extra https://www.geeksforgeeks.org/selecting-rows-in-pandas-dataframe-based-on-conditions/
#indexing/slicing

df = pd.DataFrame()
print(df)

data1 = [1,2,100]
df2 = pd.DataFrame(data1)
print(df2)
print("*")
data3 = [["cagri", "yalniz", "sarı"], ["yaşar", "yıldız", "siyah"], ["fatma", "tuğ", "beyaz"]]
print(data3)
df3 = pd.DataFrame(data3)
print(df3)

df3a = pd.DataFrame(data3, columns=["isim", "soyisim", "sac_rengi"], index=[1,2,3])
print(df3a)
print("**")

data4 = {"İsim": ["cagri", "yaşar", "fatma"],
        "Soyisim": ["yalniz", "yıldız", "tuğ"],
        "Sac_rengi": ["sarı", "siyah", "beyaz"],
        "Yaş" :[22, 39, 88]}
df4 = pd.DataFrame(data4,columns=["isim", "Soyisim", "Sac_rengi", "Yaş"]) #harf duyarliligi var. "isim" in ilk harfini kucuk yazınca ciktida oranın degerlerinin NaN dondu
print(df4) 

df4a = pd.DataFrame(data4,columns=["İsim", "Soyisim", "Sac_rengi", "Yaş"])
print(df4a) 


df4a.pop("Yaş")
print(df4a)

#df4b = df4a.pop("Yaş") yapıldıgı zaman df4b ye ustteki degeri atamıyor

print(df3a.loc[1]) #bizim verdigimiz indexle calisiyor
print(df3a.iloc[1]) #sistemin indexiyle calisiyor

print("***")

data5 = {"İsim": ["cagri", "yaşar", "fatma", "gül", "begüm", "veli", "şaban"],
        "Soyisim": ["yalniz", "yıldız", "tuğ", "dört", "kale", "saç", "ayan"],
        "Sac_rengi": ["sarı", "siyah", "beyaz", "siyah", "siyah", "sarı", "beyaz"],
        "Yaş" :[22, 39, 88, 12, 34, 39, 55]}

data5a = {"İsim": ["necip"],
        "Soyisim": ["şimşek"],
        "Sac_rengi": ["beyaz"],
        "Yaş" :[55]}

df5 = pd.DataFrame(data5, columns=["İsim", "Soyisim", "Sac_rengi", "Yaş"])
df5a = pd.DataFrame(data5a, columns=["İsim", "Soyisim", "Sac_rengi", "Yaş"])
df5b = df5.append(df5a)
print(df5b)

print("****")
print(df5b.head())
print(df5b.head(2))
print(df5b.tail(2))

print("*****")
df5c = df5b[df5b['Yaş'] > 30].sort_values(by=["Yaş"])
print(df5c)

renkler = ["sarı", "beyaz"]
df5d = df5b[df5b["Sac_rengi"].isin(renkler)].sort_values(by=["Yaş"])
print(df5d)

print("*-*-*-*-*-*-*")


def CsvOlustur():
        df5b.to_csv('df5b.csv')

def CsvSil():
        import os
        os.remove('df5b.csv')


notlar1 = pd.read_csv("notlar.csv")
print(notlar1)
print(str(len(notlar1.columns)) + " " + str(len(notlar1))) 

print(notlar1.head(3))
print(notlar1["Last name"])

notlar1.columns = ["İsim", "Soyisim", "SSN", "T1", "T2", "T3", "T4",
                "Final", "Grade"]

print(notlar1)
print(notlar1["İsim"])
print(notlar1["İsim"] + notlar1["Grade"])
notlar2 = pd.DataFrame(notlar1["İsim"]).rename(columns={" " : "İsim" ,}) #buna grade eklendigi zaman sutun ismi degismiyor, neden acaba 
print(notlar2)

print(notlar1.iloc[0])
print(notlar1.iloc[0, 1])

print(notlar1.iloc[0:1])
print(notlar1.iloc[0:1, 0:3])
print(notlar1.loc[:,"İsim"])
print(notlar1.loc[:5, "İsim": "T2"])
print(notlar1.loc[:3, ["İsim", "Final"]])

# notlar3 = pd.read_csv("notlar2.csv")
# print(notlar3)
# print(notlar3.loc[[0]])

# k = 0
# for i in notlar1.iloc[k]:
#         if notlar1.iloc[7] > 50:
#                 print("ok")

#         k = k + 1