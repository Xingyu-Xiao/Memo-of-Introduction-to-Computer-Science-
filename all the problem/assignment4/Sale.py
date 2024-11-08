n, m = map(int, input().split())
a = list(map(int, input().split()))
a.sort()
if a[m-1] <= 0:
    print(-sum(a[0:m]))
else:
    s = 0
    for x in a[:m]:
        if x <= 0:
            s += x
    print(-s)
