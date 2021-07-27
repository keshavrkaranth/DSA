'''

    super_digit(9875)->9+8+7+5 = 29
	super_digit(29)->2 + 9 = 11
	super_digit(11)->1 + 1 = 2
	super_digit(2)-> 2
'''


def superDigit(n, k):
    num = 0
    # find the sum of num
    for i in str(n):
        num += int(i)
    # multiply with occurence
    num *=k
    # recursive call
    return superDigit(num, 1) if num>9 else num

print(superDigit('420',1))

