import numpy as np
#numpy calismalari yapildi
a = np.arange(10)
b = a
print(a)
print(b)

b[0] = 100
print(a)
print(b)

#a ve b nin bellekte isaret ettigi yerler esitleniyor(referans ataması/ikisi de aynı referansı tutuyor)
#degiskenler icin gecerli olan bir durum degil. dizilerde gecerli

c = a.copy()
c[0] = 1
print("a: " + str(a))
print("c: " + str(c))


d = a.view()
print("a: " + str(a))
print("d: " + str(d))

print("***")

d[0] = 12
print("a: " + str(a))
print("d: " + str(d))



print("***")

d.shape = 2,5
print("a: " + str(a))
print("d: " + str(d))

print("***")

a[0] = 2
print("a: " + str(a))
print("d: " + str(d))