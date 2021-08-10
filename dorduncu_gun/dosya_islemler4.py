#%%
#denemeler
# yarismaciler = list()

# y1= str(input("ilk yarismaciyi giriniz"))
# yarismaciler.append(y1)

# print(yarismaciler)

#%%


def Aktarim():

    yarismaciRe = open("yarismaci.txt", "r")
#print(yarismaciRe.read()) burasi yorum satiri olmadigi zaman burayi okuyup alttaki komutta okuma islemini yapmiyordu !!!
    ayir = yarismaciRe.read().split(".")
    print(ayir)
    print(ayir[0])
    print(len(ayir))
    yeniYarismacilar = list()
   
    for i in ayir:
        yeniYarismacilar.append(i)
    
    print(yeniYarismacilar)


    yeniYarismacilarA = open("yeniyarismacilar.txt", "a")
    yeniYarismacilarA.write(str(yeniYarismacilar))
    yeniYarismacilarA.close
    yarismaciRe.close

Aktarim()

