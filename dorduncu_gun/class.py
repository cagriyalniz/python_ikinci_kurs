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
