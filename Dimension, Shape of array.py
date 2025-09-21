import numpy as np


a = np.array([[123, 87, 88],
             [2983, 39, 99]], dtype='int16')
print(a.shape)
print(a.size)
print(a.dtype)
print(a.itemsize)
print(a.nbytes)

print()

b = np.array([2.4, 8, 6],dtype='float16')
print(b.shape)
print(b.size)
print(b.dtype)
print(b.itemsize)
print(b.nbytes)
