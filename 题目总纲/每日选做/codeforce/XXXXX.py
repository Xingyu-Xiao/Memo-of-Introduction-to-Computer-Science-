t = int(input())
for i in range(t):
    n, x = map(int, input().split())
    a = list(map(int, input().split()))
    if sum(a) % x != 0:
        print(n)
    else:
        out = []
        for j in range(n):
            if a[j] % x != 0:
                out.append(max(j+1, n-j-1))
                break
        a.reverse()
        for j in range(n):
            if a[j] % x != 0:
                out.append(max(j+1, n-j-1))
                break
        if out:
            print(max(out))
        else:
            print(-1)
