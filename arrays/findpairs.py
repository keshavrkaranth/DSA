'''
write a program to find all pairs of integer whose sum is equal to given number

ex:[2,6,3,9,7,11]
no 9-> [6,3]
'''

mylist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30,
          31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57,
          58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85,
          86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]
arr = [2, 3, 4, -2, 6, 8, 9, 11];


def findPairs(list, num):
    list.sort()
    length = len(list)
    for i in range(length):
        for j in range(i + 1, length):
            if list[i] + list[j] == num:
                print(f'[{list[i]},{list[j]}]')


findPairs(arr, 6)
