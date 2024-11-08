q = int(input())
for _ in range(q):
    n = int(input())
    s = list(map(int, input().split()))
    a = {}
    for x in s:
        a[x] = a.get(x, 0) + 1
    for y in range(11):
        try:
            a[2**(y+1)] = a.get(2**(y+1), 0) + a[2**y]//2
        except KeyError:
            continue
    if 2048 in a:
        if a[2048] > 0:
            print('YES')
        else:
            print('NO')
    else:
        print('NO')
