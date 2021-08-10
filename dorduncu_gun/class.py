#%%
class Matematik:
    def tplm(self, s1, s2):
        return s1 + s2
# self onemli, classın kendisine referans

math = Matematik()
print(math.tplm(5,3))

class Matematik2:
    def toplama(self, sayi1, sayi2):
        sonuc = int(sayi1) + int(sayi2)
        print(sonuc)
        return sonuc

matematik22 = Matematik2()
matematik22.toplama(1,2)

class Sekil:
    def kare(self, en):
        kareAlan = int(en) * int(en)
        return kareAlan

    def dikUcgen(self, taban, yukseklik):
        dikUcgenAlan = int(taban) * int(yukseklik) / 2
        return dikUcgenAlan

sariUcgen = Sekil()
print("sari ucgenin alani: " +  str(sariUcgen.dikUcgen(12, 6)))

class SekilOzellik:
    def __init__(self, renk, kenarSayi, en, boy):
        self.rengi = renk
        self.kenarSayisi = kenarSayi
        self.eni = en
        self.boyu = boy
    def alan(self):
        return self.eni * self.boyu
    
    def cevre(self):
        return self.eni*2 + self.boyu*2
        
dikDortgen = SekilOzellik("kirmizi", 4, 10, 5)
print(str(dikDortgen.rengi), dikDortgen.kenarSayisi)
print(dikDortgen.eni, dikDortgen.boyu)
print(dikDortgen.alan(), dikDortgen.cevre())


class Canli():
    def fiziki(self, cins, yas, boy, kilo):
        return cins, yas, boy, kilo
    
class Insan(Canli):
    def hareket(self):
        return "yürüyebilir"

cagri = Canli()
print("cagri: " + str(cagri.fiziki("insan", 26, 168, 78)))

ali = Insan()
print(ali.fiziki("insan", 22, 120, 190))
print(ali.hareket())

class Hasta():
    def __init__(self, ad, soyad, tc, telefon) -> None:
        self.name = ad
        self.surname = soyad
        self.id = tc
        self.phonenumber = telefon
        
    def kanTahlil(self, sonuc):
        self.tahlilSonuc = sonuc
        return self.id, sonuc

    def safSes(self, sso):
        self.isitme = sso
        return self.id, sso


hasta1 = Hasta("cagri", "yalniz", 2222, 5051)
print(hasta1.safSes(75))
print(hasta1.kanTahlil("covid +"))

class Musteri(Hasta):
    def __init__(self, ad, soyad, tc, telefon, borc) -> None:
        super().__init__(ad, soyad, tc, telefon)
        self.borc = borc

    def odeme(self, islem, islemUcreti, odenenTutar):
        self.yapilanIslem = islem
        self.fatura = islemUcreti
        self.yatirilanPara = odenenTutar
        self.borc = int(islemUcreti) - int(odenenTutar)
        return self.id, islem, islemUcreti, odenenTutar, self.borc

Musteri1 = Musteri("ayşe", "kal", 123, 100, 0)
print(Musteri1.odeme("muayene", 1200, 1100))


# class Birey:
#     def kisiselBilgi(self, ad, soyad, yas):
#         return ad, soyad, yas

# insan1 = Birey()
# print(insan1.kisiselBilgi("cagri", "yalniz", 26))
# insan1.kisiselBilgi = "cagri", "yalniz", 26
# print(insan1.kisiselBilgi)

# class Birey2():
#     def adi(self, name):
#         return name

# insan2 = Birey2()
# insan2.adi = "cagri"
# print(insan2.adi)





# class Person:
#     def __init__(self, firstName, lastName, age) -> None:
#         self.firstName = firstName
#         self.lastName = lastName
#         self.age = age

# birey = Person("cagri", "yalniz", 26)
# print(birey.firstName)


# class Customer(Person):
#     def __init__(self, firstName, lastName, age, cardNumber) -> None:
#         super().__init__( firstName, lastName, age)
#         self.cardNumber = cardNumber

# ali2 = Customer("ali2", "al", 11, 123)

# class Patient(Person):
#     def __init__(self, firstName, lastName, age, rh) -> None:
#         super().__init__(firstName, lastName, age)
#         self.rh = rh
#         sonuc = "{} yasindaki hasta {} {} , {} kan grubuna sahip ".format(age, firstName, lastName, rh)
#         return sonuc
        


# hasta2 = Patient("veli", "kırk", 12, "AB")
# print(hasta2)




# class Rectangle:
#     def __init__(self, length, width):
#         self.length = length
#         self.width = width

#     def area(self):
#         return self.length * self.width

#     def perimeter(self):
#         return 2 * self.length + 2 * self.width

# class Square(Rectangle):
#     def __init__(self, length):
#         super().__init__(length, length)

# kare = Square(4)
# print(kare.area())
# print(kare.perimeter())
# %%
