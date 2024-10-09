a = int(input())
factors = []
while a % 2 == 0:
    factors.append(2)
    a = a//2
while a % 3 == 0:
    factors.append(3)
    a = a//3
for i in range(5, int(a**0.5)+1, 6):
    while a % i == 0:
        factors.append(i)
        a = a//i
    while a % (i+2) == 0:
        factors.append(i+2)
        a = a//(i+2)
if a > 2:
    factors.append(a)
f = 0
for x in factors:
    n = factors.count(x)
    if n != 1:
        f = 1
if f == 1:
    print(0)
else:
    if len(factors) % 2 == 0:
        print(1)
    else:
        print(-1)
