'''
Sample Input

cde
abc
Sample Output

4
Explanation

Delete the following characters from the strings make them anagrams:

Remove d and e from cde to get c.
Remove a and b from abc to get c.
It takes 4 deletions to make both strings anagrams.
'''

a = 'fcrxzwscanmligyxyvym'
b = 'jxwtrhvujlmrpdoqbisbwhmgpmeoke'
d = {}
count = 0
for i in a:
    d.setdefault(i, 0)
    d[i] = d[i]+1

for i in b:
    d.setdefault(i, 0)
    d[i] = d[i]+1

for i in d.values():
    if i > max(list(d.values())):
        continue
    else:
        count += 1


print(sum(d.values()))
print(d)
print()
print(count)
