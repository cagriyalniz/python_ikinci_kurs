import numpy as np
#numpy calismalari yapildi
#/linspace/pi/sin

x = np.linspace(1,10)
print(x)

y = np.linspace(1,10,10) #1 den 10 a kadar esit araliklari bulunan 10 sayi uret
print(y)

z = np.linspace(1,10,3) #1 den 10 a kadar esit araliklari bulunan 3 sayi uret
print(z)
print(str(z[1]) + "---" + str(len(z)))

from numpy import pi

a = np.linspace(0,2*pi,100) #0 derece ile 360 derece arasındaki 100 deger
print(a)
print(np.sin(x)) # o derecelerin sinüs degerleri. lakin ben bunun boyle olduguna inanmadim. cunku açıların sinusu alınınca cikan sonucla asagıda sonuc eslesmiyor
print(a[1])
print(np.sin(x)[1])


b = np.linspace(0, pi,3)
print(b)