'''
Question 2
Given two non-negative integers n1 and n2, where n1<n2. The task is to find the total number of integers in the range [n1, n2](both inclusive) which have no repeated digits.

For example:
Suppose n1=11 and n2=15.
There is the number 11, which has repeated digits, but 12, 13, 14 and 15 have no repeated digits. So, the output is 4.

Example1:
Inout:
11 --- Vlaue of n1
15 -- value of n2

Output:
4

Example 2:
Input:
101 -- value of n1
200 -- value of n2

Output:
72

'''


n1 = 11
n2 = 15
count = 0
for i in range(n1,n2+1):
    pass