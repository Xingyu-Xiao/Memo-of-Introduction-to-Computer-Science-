import math
n = int(input())
s = []
for j in range(n):
    a, b, c = map(float, input().split())
    s.append([a, b, c])
for ss in s:
    a = ss[0]
    b = ss[1]
    c = ss[2]
    if b == 0:
        b = -b
    k = b**2 - 4*a*c
    p = -b/(2*a)
    if k == 0:
        print(f'x1=x2={p:.5f}')
    elif k > 0:
        x1 = p + (math.sqrt(k))/(2*a)
        x2 = p - (math.sqrt(k))/(2*a)
        print(f'x1={x1:.5f};x2={x2:.5f}')
    elif k < 0:
        kk = (math.sqrt(-k))/(2*a)
        print(f'x1={p:.5f}+{kk:.5f}i;x2={p:.5f}-{kk:.5f}i')
