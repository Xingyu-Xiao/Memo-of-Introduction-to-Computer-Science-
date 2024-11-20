import math

a = input()
s = set([i**2 for i in range(1, int(math.sqrt(int(a)))+1)])
ans = []


def f(i=0, j=0):
    while i < len(a) and j < len(a):
        if int(a[i:j+1]) in s:
            f(i, j+1)
            i = j+1
            j = i
        else:
            j += 1
    if j == i:
        ans.append(0)
    return


f()
if ans:
    print('Yes')
else:
    print('No')
