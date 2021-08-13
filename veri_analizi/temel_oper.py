#https://numpy.org/
#numpy calismalari yapildi
#temel operatorler

import numpy as np
from numpy.lib.function_base import percentile
from numpy.lib.stride_tricks import broadcast_shapes

a = np.array([1, 10, 100])
b = np.arange(3)

c = a - b
print("a: " + str(a))
print("b: " + str(b))
print("a - b: " + str(c))

e = 10*np.sin(a)
print(e)
sinList = list()
for i in e:
    if i < 7:
        print("deger 7'den kucuk, listeye eklendi")
        sinList.append(i)
    else:
        print("deger 7den buyuk: {}".format(i))
print("liste: " + str(sinList))

print(a@b) # = a.dot(b) = matris carpimi demek

c = np.zeros((2,4)) #2 ye 4 lük sıfırlar olustur (2 satır 4 sutun)
d = np.ones((3,3))
print(c)
print(d)

e = np.random.random((2, 4))
print(e)

f = np.random.randint((15))
print(f)

for i in range(20):
    g = np.random.randint((20))
    print(g)

for i in range(10):
    g = np.random.randint(10, size = 2)
    print(g)
    print(g[0])


g = np.random.random_integers(4, size = (3,2))
print(g)

g1 = np.random.random_integers(1,6, 10)
g2 = np.random.random_integers(1, 6, 10)
print(g1)
print(g2)
print(g1 + g2)
print(np.sum(g1))
print(np.min(g1))
print(np.max(g1))
print(np.size(g1))
print(np.sort(g1))

g3 = np.random.random_integers(1,10000, 50)
print(np.sort(g3))
