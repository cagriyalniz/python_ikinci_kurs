
try:
    sayi = int(input("bir sayi giriniz: "))

except ValueError:
    print("sayi giriniz, baska karakter degil")
except:
    print("hata: sayi girisi yapilmadi") #üstteki kodda hata meydana geldigi zaman calisacak

print("finish")

try:
    print("bolme islemi icin")
    sayi1 = int(input("ilk sayiyi giriniz: "))
    sayi2 = int(input("ikinci sayiyi giriniz: "))
    sayi3 = sayi1/sayi2
    print(sayi3)
except(ValueError, ZeroDivisionError):
    print("sayi girmeniz lazim ve ikinci sayi sifir olamaz")

my_list = [12, "cagri", "12", 0]
k = 1
for i in my_list:
    try:
        print("listenin {}. elemani: ".format(k) + str(i)) #bu for donguleri icine surekli bir sayac sıkıstırıyorum. bunun baska bir yolu olmasi lazim. belki ic ice for dongusu yazmam gerekiyordur bilmiyorum
        sonuc = 1/int(i)
        print("sonuc: " + str(sonuc) )
        k = k + 1

    except(ValueError):
        print("sayi olmayan eleman ile bolme islemi yapilamaz")
        print("sayi olmayan eleman: " + i)
        k = k + 1

    except(ZeroDivisionError):
        print("hicbir sayi sifira bolunemez!")

    finally:
        print("islemler bitti")

