# misssing numbers b/n 1-100 n(n+1)/2
import time
st=time.time()

mylist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30,
          31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57,
          58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85,
          86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]

# approach-1

for i in range(len(mylist) -1):
    if mylist[i] + 1 == mylist[i + 1]:
        continue
    print(mylist[i] + 1)


def missingNumber(list, n):
    sum1 = n * (n + 1) / 2
    sum2 = sum(list)

    return int(sum1 - sum2)



print(missingNumber(mylist,100))
