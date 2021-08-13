import numpy as np
from numpy.core.shape_base import hstack, vstack
from numpy.lib.shape_base import hsplit, vsplit
#shape ve stack ve biraz split
s1 = np.floor(np.random.random((3,4)))
print(s1)

s2 = np.floor(10*np.random.random((3,4)))
print(s2)

print("*******")

print(s2.shape)
print(s2.ravel())
#print(s2[5]) bu kod patlıyor
print(s2.ravel()[5])
print(type(s2))
print(type(s2.ravel()))
s2 = s2.ravel()
print(s2)
s2 = s2.reshape(3,4)
print(s2)
print(s2.T) #transpose
print("******* stack ******")

s3 = np.floor(10*np.random.random((2,3)))
s4 = np.floor(10*np.random.random((2,3)))
print(str(s3) + "\n" + str(s4)) 
s5 = vstack((s3, s4))
print(s5)
print("**")
s6 = hstack((s3, s4))
print(s6)

s7 = hsplit(s6, 6)
print(s7)
print(s7[0])

s8 = vsplit(s6, 2)
print(s8)
print(s8[0])