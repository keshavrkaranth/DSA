'''


112=4
13452=15
'''

#
def sum_of_numbers(num):
    if num <= 0:
        return 0
    return int(num%10)+sum_of_numbers(num//10)

print(sum_of_numbers(148148148))

# other method
def sum_of_numbers(num):
    res = 0
    for i in str(num):
        res += int(i)
    return res


print(sum_of_numbers(148148148))
