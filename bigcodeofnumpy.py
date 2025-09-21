import numpy as np

a = np.array([[957, 579, 759, 99, 88, 12],
            [12, 372, 279, 289, 911, 65]])

#get specific element, specify row and column
print(f"{a[1, 4]}, What's your emergency?")

#get whole row
print(a[0, :])
#get some part of row
print(a[0, :5])

#get whole column
print(a[:, 3])
#get some part of column
print(a[1:, 3])

#fancier method of indexing (row, start:end:step)
print(a[0, 1:-1:2])

#changing element
a[1, 2] = 15
print(a)

#changing whole row
a[1] = [6, 12, 18, 24, 30, 36]
print(a)

#chaning whole column
a[:, 2] = [16, 32]
print(a)

#in 3d

b = np.array([
   [[21, 32, 45],
    [90, 87, 23]],

   [[3,6,9],
    [12, 15, 18]]
])

print(b.shape)
print(b[1, 0, 2])
b[1, 0, [1, 2]] = 69, 96 # double assignment of 6 and 9 to 69 & 96 respectively
print(b)
