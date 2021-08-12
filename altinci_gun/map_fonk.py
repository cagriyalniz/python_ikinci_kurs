liste1 = [1 , 2, 3]
print("birinci liste: " + str(liste1))
liste2 = list()

for sayi in liste1:
    liste2.append(sayi*sayi)

print("ikinci liste: " + str(liste2))

#liste mapping
liste3 = list(map(lambda sayi: sayi**2, liste2 ))
print("ucuncu liste: " +str(liste3))

#sozluk mapping
sozluk = {"birinci eleman" : "cagri"}
sozluk2 = dict(map(lambda s: (s[0], s[1]), sozluk.items() ))
print(sozluk2)

sozluk3 = {"1" : "bir", "2" : "iki"}
sozluk4 = dict(map(lambda s: (s[0], s[1]), sozluk3.items()))
print(sozluk4)

#set mapping
set1 = {"ayasli ve kiracilar", "miskinler tekkesi", "serguzest", "hep o sarki"}
set2 = set(map(lambda s: s, set1))
print(set2)

