import numpy as np
myArray = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])

max = 0

for i in range(len(myArray)):
    for j in range(i+1,len(myArray)):
        if myArray[i]*myArray[j]>max:
            max = myArray[i]*myArray[j]
            pairs = f"{myArray[i]},{myArray[j]}"
print(pairs)
print(max)