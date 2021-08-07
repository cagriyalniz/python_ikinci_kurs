firstStrings = "yağmur"
secondStrings = "YAĞMUR"

if (firstStrings.upper() == secondStrings.upper()):
    print("ikisi aynı")
else:
    print("ikisi aynı değil")

cumle1 = "'kaşları ne pek kalın, ne pek ince, fakat biraz kısaydı; koyu kumral saçları, köşeli ve oldukça geniş alnını çevreleyerek aşağı doğru uzanıyorlar ve yabankedisinin tüylerine karışıyorlardı sabahattin ali"
print(len(cumle1))

print(cumle1.split("k"))

ad = input("adınız:")
print(ad)

sayi1 = input("ilk sayiyi giriniz")
sayi2 = input("ikinci sayiyi giriniz")

if (int(sayi1) + int(sayi2) >= 50 ):
    print("sayilarin toplami elliden büyük", int(sayi1) + int(sayi2))
else:
    print("sayilarin toplami yeterli küçüklükte: ", int(sayi1) + int(sayi2))

x = 10
y = 50
z = 1

z=x
x=y
y=z
print(x)
print(y)

#python'ın güzelliği:
a = 30
b = 99
a,b = b,a
print(a,b)

donusum= 0.314598
ilkDeger = int(input("ilk degeri giriniz"))
donusen= ilkDeger*donusum

print("girilen deger " + str(ilkDeger) + " fakat donustukten sonraki deger:" + str(donusen))