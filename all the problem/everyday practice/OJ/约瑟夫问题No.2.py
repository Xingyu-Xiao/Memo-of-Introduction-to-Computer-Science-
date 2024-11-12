s = []
while True:
    a = tuple(map(int, input().split()))
    if a == (0, 0, 0):
        break
    else:
        s.append(a)
for ss in s:
    n, p, m = ss
    o = [i for i in range(n+1)]
    x = (m+p-1) % n
    if x != 0:
        print(o.pop(x), end=',')
    else:
        print(o.pop(n), end=',')
    while n > 2:
        n -= 1
        if x != 0:
            x = (x+m-1) % n
        else:
            x = m % n
        if x != 0:
            print(o.pop(x), end=',')
        else:
            print(o.pop(n), end=',')
    print(o[-1])