#https://www.geeksforgeeks.org/python-program-for-linear-search/

# Problem: Given an array arr[] of n elements, write a function to search a given element x in arr[].
# Examples :

# Input : arr[] = {10, 20, 80, 30, 60, 50, 
#                      110, 100, 130, 170}
#           x = 110;
# Output : 6
# Element x is present at index 6

import numpy as np
from numpy.core.fromnumeric import size
from numpy import random
#benim yontemim
randomArray = random.randint(10, size=(8))
print(randomArray)
x = random.choice(randomArray)
print(x)

sycSayi = 0
sycIndex = 0
for i in randomArray:
    if x!=i:
        sycIndex = sycIndex +1 

    else:
        print("bulunan sayi: {}, sayinin indexi: {}".format(x, sycIndex)) 


print("************")

#sitenin yontemi
def DizininSayiIndexiniBul():
    randomArray = random.randint(10, size=(8))
    print(randomArray)
    x = random.choice(randomArray)
    print(x)
    for i in range(len(randomArray)):
        if randomArray[i] == x:
            print(i)
    
DizininSayiIndexiniBul()

