import numpy as np
#numpy calismalari yapildi
#arange/reshape/ndim

# havaDurumu = [12, 10, 15, -2, -5, 0, 5, 6, 3]
# print("hava durumu type: " + str(type(havaDurumu)))
# print("hava durumu: " + str(havaDurumu))


# def Olusturma():

#     dimensionCountW = open("Dimension Count.txt", "w")
#     hD = np.arange(2).reshape(2)
#     yazdir1 = "hD--- dimension count: " + str(hD.ndim) + "\n" + str(hD) + "\n"

#     hP = np.arange(6).reshape(2,3)
#     yazdir2 = "hP--- dimension count: " + str(hP.ndim) + "\n" + str(hP) + "\n"
    
#     hF = np.arange(24).reshape(2,3,4)
#     yazdir3 = "hF--- dimension count: " + str(hF.ndim) + "\n" + str(hF) + "\n"

#     hT = np.arange(120).reshape(2,3,4,5)
#     yazdir4 = "hT--- dimension count: " + str(hT.ndim) + "\n" + str(hT) + "\n"

#     dimensionCountW.write(yazdir1)
#     dimensionCountW.write(yazdir2)
#     dimensionCountW.write(yazdir3)
#     dimensionCountW.write(yazdir4)
    

#     dimensionCountW.close()


# def Silme():
#     import os 
#     os.remove("Dimension Count.txt")

#Silme()
#Olusturma()


# x = np.array([1, 2, 3, 4, 5, 6]) #array fonksiyonuna [1,2,3,4,5,6] degeri verildi
# print(x)
# print(type(x))
# print(x.dtype)

# y = np.array(["a", "b"])
# print(y.dtype)

# z = np.array(["a", "5"])
# print(z.dtype)

# a = np.array([[1,3], [2,5], [3, 7]])
# print(a)
# print(a.ndim)

# print(x.reshape(2,3))



