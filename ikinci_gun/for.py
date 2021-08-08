code = [4 , 8 , 15 , 16 , 23 , 42]

for num in code:
    print(num)

for num in code:
    if num >= 16:
        print(num)
    else:
        print("sayi cok kucuk")

meyveler = [ ]
for i in range(3):
    meyveler.append(input("{}. meyvenin ismini yaziniz \n".format(i + 1))) #gereksiz kod var mı ?

print(meyveler)


