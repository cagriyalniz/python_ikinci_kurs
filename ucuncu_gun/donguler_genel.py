cumle1 = "eğer şu şekilde başlasaydım her şey farklı olurdu: size söyleyeceklerimi söylemeye değecek mi bilmiyorum, çünkü beyni sulanmış bir aptal kitlesine sesleneceğimi çok iyi biliyorum; ama salonda bulunan, aptal çoğunluğun dışında kalan iki üç kişiye olan saygım nedeniyle konuşuyorum"


cumle2 = cumle1.split(" ")
print(cumle2)
print(cumle2[0])

for i in range(len(cumle2)):
    print(cumle2[i])


#temel mantik:
# t = 0
# for i in cumle2:
#     print(cumle2[t])
#     t = t + 1
    
x = 0
syc_tr = 0

for i in cumle2:
    if i == "ç" or "ğ" or "ı" or "ö" or "ü" or "ş":
        
        print(i)
        syc_tr = syc_tr + 1
        cumle2[x] = cumle2[x].replace("ç", "c")
        cumle2[x] = cumle2[x].replace("ğ", "g")
        cumle2[x] = cumle2[x].replace("ı", "i")
        cumle2[x] = cumle2[x].replace("ö", "o")
        cumle2[x] = cumle2[x].replace("ş", "s")
        cumle2[x] = cumle2[x].replace("ü", "u")
    x = x + 1

print(cumle2)
print("bu cumlede {} adet turkce karakter mevcut".center(60, "*").format(syc_tr))

print(len(cumle1))
print(len(cumle2))

cumle3 = ""

syc = 0
for i in cumle2:
    cumle3 = cumle3 + " "
    cumle3 = cumle3 + cumle2[syc]
    syc = syc + 1 


print(cumle3.strip())
print(len(cumle3.strip()))

syc_a = 0
for i in cumle3.strip():
    if i == "a":
        syc_a = syc_a + 1

print("bu cumlede " + str(syc_a) + " tane a harfi var")
