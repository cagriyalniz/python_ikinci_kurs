import numpy as np

# havaDurumu = [12, 10, 15, -2, -5, 0, 5, 6, 3]
# print("hava durumu type: " + str(type(havaDurumu)))
# print("hava durumu: " + str(havaDurumu))


# hD = np.arange(2).reshape(2)
# print("hD type: " + str(type(hD)))
# print("hD: \n" + str(hD))
# print("Dimension Count: " +str(hD.ndim)) #boyut sayisi

# hP = np.arange(6).reshape(2,3)
# print("hP: \n" + str(hP) + "\n" + "dimension count: " + str(hP.ndim))

# hF = np.arange(24).reshape(2,3,4)
# print("hF: \n" + str(hF) + "\n" + "dimension count: " + str(hF.ndim))

# hT = np.arange(120).reshape(2,3,4,5)
# print("hT: \n" + str(hT) + "\n" + "dimension count: " + str(hT.ndim))

def Olusturma():

    dimensionCountW = open("Dimension Count.txt", "w")
    hD = np.arange(2).reshape(2)
    yazdir1 = "hD--- dimension count: " + str(hD.ndim) + "\n" + str(hD) + "\n"

    hP = np.arange(6).reshape(2,3)
    yazdir2 = "hP--- dimension count: " + str(hP.ndim) + "\n" + str(hP) + "\n"
    
    hF = np.arange(24).reshape(2,3,4)
    yazdir3 = "hF--- dimension count: " + str(hF.ndim) + "\n" + str(hF) + "\n"

    hT = np.arange(120).reshape(2,3,4,5)
    yazdir4 = "hT--- dimension count: " + str(hT.ndim) + "\n" + str(hT) + "\n"

    dimensionCountW.write(yazdir1)
    dimensionCountW.write(yazdir2)
    dimensionCountW.write(yazdir3)
    dimensionCountW.write(yazdir4)
    

    dimensionCountW.close()

    



def Silme():
    import os 
    os.remove("Dimension Count.txt")

Silme()
Olusturma()