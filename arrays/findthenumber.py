import numpy as np
myArray = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])
l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]



# simple method with list
if 12 in l:
    print(l.index(12))


# using array

def findNumber(list,num):
    for i in range(len(myArray)):
        if myArray[i] == num:
            print(i)

findNumber(myArray,12)