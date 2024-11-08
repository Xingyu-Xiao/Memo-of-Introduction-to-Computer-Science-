t = int(input())
for i in range(t):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    tu = [(a[i], i) for i in range(n)]
    tu.sort()
    b.sort()
    s = [0]*n
    for j in range(n):
        _, index = tu[j]
        s[index] = str(b[j])+' '
    print(''.join(s))
