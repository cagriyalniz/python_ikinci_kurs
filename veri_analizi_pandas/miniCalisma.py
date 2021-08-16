import pandas as pd

filmler = pd.read_csv("imdb-1000.csv")
#print(filmler.loc[:, "title"] == "Pulp Fiction")
#print(filmler["title"] == "Pulp Fiction")

#print(ax)
# if filmler["title"] == "Pulp Fiction":
#     print(filmler["title"])

# for i in ax:
#     if i == True:
#         print(i)
    
# print(len(filmler))
# print((filmler.loc[2])[['title']])

# queryy = (filmler.loc[2])[['title']]
# print(queryy)


# for i in range(len(filmler)):
#     sorgu1 = (filmler.loc[i])[['title']]
#     sorgu2 = str(sorgu1).split(" ")
#     for k in sorgu2:
#         if k == "The":
#             print((filmler.loc[i])[['title']])
#             syc = syc + 1
# print("{} adet THE iceren film var".format(syc))

#film isimlerinde en cok kullanilan kelimeleri bulmaya calistim
#film isimlerini kelime halinde listeye atmaya calistim(kelime tekrari olmadan)

# print((filmler.loc[1])[['title']])
# print(len((filmler.loc[1])[['title']]))
# sorgu1 = (filmler.loc[1])[['title']]
# sorgu2 = str(sorgu1).split(" ")
# print(sorgu2)
# print(len(sorgu2))
# print(sorgu2[2])

# deliListe1 = list()
# deliListe1.append(sorgu2)

# print(deliListe1)

# deliListe25 = list(('title', "The"))
# listeSonPls = list()
print("********************")
# for i in range(len(deliListe25)):
#     print(deliListe25)

# print(deliListe25[0])

# for k in sorgu2:
#     print(k)
# print("*********************")

# for i in deliListe2:
#     for k in sorgu2:
#         if k !=i:
#             listeSonPls.append(k)
# print(listeSonPls)

# for i in range(len(sorgu2)):
#     for k in sorgu2[i]:
#         if deliListe2 != k:
#             deliListe2.append(sorgu2[i])

# print(deliListe2)


print("bismillah")
deliListe = list()
syc2 = 0
syc31 = 0
for i in range(len(filmler)):
    sorgu1 = (filmler.loc[i])[['title']]
    
    sorgu2 = str(sorgu1).split(" ")
    print(sorgu2)

    for t in deliListe:
        if k == t:
            syc31 = syc31 + 1                         
        else:
            deliListe.insert(syc2,k)
            syc2 = syc2 + 1


# for k in sorgu2:
#     print(k)
#     for t in deliListe:
#         print(t)
#         if k == t:
#             print("eşit aq")
#         else:
#             deliListe.insert(syc2,k)
#             syc2 = syc2 + 1
# for t in sorgu2:
#     deliListe.insert(syc2,t)
    #syc2 = syc2 + 1
print(deliListe)