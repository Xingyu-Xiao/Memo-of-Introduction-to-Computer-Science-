s = []
while True:
    a = list(map(int, input().split()))
    if a == [0, 0]:
        break
    else:
        s.append(a)
for ss in s:
    n, m = ss
    p = [i for i in range(1, n+1)]
    if n == 1:
        print(1)
    else:
        del p[m % n - 1]
        x = m % n
        n -= 1
        while len(p) > 1:
            if x == 0:
                del p[m % n - 1]
                x = m % n
            else:
                del p[((m % n) + x - 1) % n - 1]
                x = ((m % n) + x - 1) % n
            n = n - 1
        print(p[0])
