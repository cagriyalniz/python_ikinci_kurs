ogrenciSeti = {"kerem", "semih", "ahmet"}
print(ogrenciSeti)

#alttaki kod çalışmaz çünkü setlerde sıra yok
#print(ogrenciSeti[0])



keremCount=0
keremUncount=0
for ogrenci in ogrenciSeti:
    if(ogrenci == "kerem"):
        keremCount = keremCount + 1 

    else:
        keremUncount = keremUncount + 1

print("kerem olmayan kişi sayısı: " + str(keremUncount))
print("kerem olan kişi sayısı: " + str(keremCount))

print("merve" in ogrenciSeti)

print(len(ogrenciSeti))

ogrenciSeti.add("ali")
ogrenciSeti.update(["mahmut", "yusuf", "gulsah"])
print(ogrenciSeti)
print(len(ogrenciSeti))

ogrenciSeti.remove("ali")
ogrenciSeti.discard("ali") #aynı elemanı iki kere silerken ikinci silinmede hata vermemeyi saglar

setA = {1, 2, "a"}
setB = {1, "a", "b"}

print(setA.union(setB))