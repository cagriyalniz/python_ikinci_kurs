f = open("musteriler.txt")
#print(f.read())
#ustteki kod ile okuma islemini gerceklestirdikten sonra
#alttaki kod hicbir sey print etmiyor cunku
#ustteki kod ile okuma islemini tamamladi, okunacak bir sey kalmadı

# print(f.read(1))

# print(f.readline())
# print(f.readline())

# for l in f:
#     print(l)

f.close()

filedToAppend = open("ogrenciler.txt", "a")
filedToAppend.write("\ncagri")
filedToAppend.close()

# dosyayi silme islem:
# import os 
#os.remove("ogrenciler.txt")

