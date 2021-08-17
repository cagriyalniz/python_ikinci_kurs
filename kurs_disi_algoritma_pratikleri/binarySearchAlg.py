#https://www.geeksforgeeks.org/python-program-for-binary-search/

# Compare x with the middle element.
# If x matches with the middle element, we return the mid index.
# Else if x is greater than the mid element, then x can only lie in the right 
# (greater) half subarray after the mid element. 
# Then we apply the algorithm again for the right half.
# Else if x is smaller, the target x must lie in the left (lower) half. 
# So we apply the algorithm for the left half.

import numpy as np
from numpy import array, random
from numpy.core.fromnumeric import sort

randomArray = np.random.randint(100, size=(9))
print(randomArray)

#random array olusturmak guzel oldu fakat arrayin boyutunu belirledigimiz icin eleman eklemesi yapamadik
my_array = [2, 3, 4, 10, 40 ]
randomX =np.random.randint(100)

for i in range(9):
    rX = np.random.randint(100)
    my_array.append(rX)

print("my array: {}".format(my_array))
#siraliMyArray = sort(my_array) #yav ben bu siralama islemini for dongusuyle yapacaktım ama sonra biraz da python ın nimetlerinden yararlanmak istedim (: 
#sort yapinca da append fonk calismiyor


mid1 = int(len(my_array)/2)
sycIndex=0
for i in range(len(my_array)):
    if randomX > my_array[mid1]:
        my_array = [my_array[mid1 + 1], my_array[mid1 +2]]
        
    else:
        


