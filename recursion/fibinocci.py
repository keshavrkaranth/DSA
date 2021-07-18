"""
This function calculates the Fibonacci num till the given range
0,1,1,2,3,5,8,13,21....
basically it is the sum of the previous two numbers and it starts from 0 and 1
"""

def fibinocci(num):
    assert 0 <= num == int(num), 'Fibinocci number cannot be negative integer or nor integer'
    if num in [0,1]:
        return num
    else:
        return fibinocci(num-1)+fibinocci(num-2)


print(fibinocci(9))


'''to print sequence'''
# for i in range(9):
#     print(fibinocci(i),end=' ')