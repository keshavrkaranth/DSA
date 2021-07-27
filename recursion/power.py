


def power(num,exp):
    if exp<=0:
        return 1
    if exp == 1:
        return num
    return num*power(num,exp-1)

print(power(3,6))