import math

a = int(input())
s = []
for i in range(a):
    s.append(int(input()))
for x in s:
    n = int(math.log2(x))
    out = (1+x)*x//2 - 2*(2**(n+1)-1)
    print(out)
