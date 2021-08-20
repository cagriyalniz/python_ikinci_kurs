#https://www.geeksforgeeks.org/python-program-for-insertion-sort/

# Insertion sort is a simple sorting algorithm that works the way 
# we sort playing cards in our hands.

# def Deneme(arrX):

#     dizinUzunluk = len(arrX)
#     print(arrX, dizinUzunluk, type(arrX))
# dizim= [1,2,3]
# Deneme(dizim)

def Siralama(arrX):
    dizinUzunluk = len(arrX) - 1
    bos = 0
    dolu = 1
    for i in range(dizinUzunluk):
        if arrX[i] > arrX[i+1]:
            bos = arrX[i]
            arrX[i] = arrX[i+1]
            arrX[i + 1] = bos
            
        else:
            i = i


    print(arrX)

    

diziOrnegi = [2 ,100, 1, 3, 101, 4]
Siralama(diziOrnegi)   
# 2 1 3
# 1 2 3
