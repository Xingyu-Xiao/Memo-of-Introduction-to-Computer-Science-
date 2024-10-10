n, d = map(int, input().split())
a = [int(input()) for _ in range(n)]
a.sort()
for index, x in enumerate(a):
    if index < len(a)-1:
        s = [str(x), str(a[index+1])]
        ss = sorted(s)
        if abs(x-a[index+1]) <= d and ss != s:
            a[index] = a[index+1]
            a[index+1] = x
for y in a:
    print(y)
