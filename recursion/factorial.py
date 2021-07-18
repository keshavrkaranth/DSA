"""
This function calculates the factorial of a number using recursion.
"""

def factorial(num):
    if num>=0 and num==int(num):
        if num == 0 or num ==1:
            return 1
        else:

            return num*factorial(num-1)
    return -1

print(factorial(25))