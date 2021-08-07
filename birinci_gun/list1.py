
my_list = ["kocaeli" , "istanbul" , "londra"]
print(my_list)
print(my_list[1])

my_list.append("urfa")
print(my_list)

my_list.remove("urfa")
print(my_list)

my_list[0], my_list[1] = my_list[1], my_list[0]
print(my_list)

#list constructor
ulkeler = list(("türkiye", "almanya"))
print(ulkeler)

print(len(my_list))
print(my_list.clear())

ogrenci_listesi = ["ali", "ayşe", "faruk", "mithat", "derya", "buse", "ali veli"]
print(ogrenci_listesi.count("ali"))

ogrenci_listesi.pop(2)
ogrenci_listesi.insert(2, "gül")
print(ogrenci_listesi)

#copy özelliği önemli
ogrenci_listesi2 = ogrenci_listesi.copy()
ogrenci_listesi2[0] = "kazım"
print("birinci liste: ", ogrenci_listesi)
print("ikinci liste: ", ogrenci_listesi2)

ogrenci_listesi3 = ogrenci_listesi
ogrenci_listesi3[0] = "mustafa"
print("birinci liste de degisti: ", ogrenci_listesi)
print("ucuncu liste: ",  ogrenci_listesi3)

ogrenci_listesi.extend(ulkeler)
print(ogrenci_listesi)

