'''
inp = [1,2,3,4]

out = [24,12,8,6]


'''
inp = [1, 2, 3, 4]
res = []


# with dividing


for i in range(0, len(inp)-1):
    for j in range(i, len(inp)-1):
        res.append(inp[i]*inp[j])

print(res)
