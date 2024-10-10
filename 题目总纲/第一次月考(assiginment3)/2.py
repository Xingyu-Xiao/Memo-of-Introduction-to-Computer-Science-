s = list(input().split())
d = {'1','2','3','4','5','6','7','8','9','0'}
a = []
for x in s:
    b = []
    for y in x:
        if y in d:
            b.append(y)
    a.append(int(''.join(b)))
print(sum(a))

