
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