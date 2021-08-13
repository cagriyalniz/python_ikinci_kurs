import numpy as np
#numpy calismalari yapildi

s1 = np.array([1, 2, 100])
print(s1[0])
print(s1[: : -1]) #tersten dizme tek boyutlu dizilerde olur
s2 = np.array([[1,2,3], [3,33, 333]])
print(s2[1])
print(s2[1,1])
print(s2[:1])
print(s2[0,1]) #sıfırncı satırdan (virgulun solu satir) 1 i ver
print(s2[:,1]) #tüm satırlardan(virgulun solu satir) 1 i ver
print(s2[:,1:2]) #tüm satırların 1 ile 2 arasını ver 2 dahil degil
print(s2[:,-1])
print(s2[-1,:])
print("***********")
for i in s2:
    print(i)