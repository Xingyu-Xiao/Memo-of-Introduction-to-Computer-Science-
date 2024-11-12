a = int(input())
s = []
for i in range(a):
    ss = int(input())
    s.append(ss)
for x in s:
    j = 0
    n = 0
    while x % 3 == 0:
        x = x//3
        j += 1
    while x % 2 == 0:
        x = x//2
        n += 1
    if x == 1 and n <= j:
        print(2*j-n)
    else:
        print(-1)
