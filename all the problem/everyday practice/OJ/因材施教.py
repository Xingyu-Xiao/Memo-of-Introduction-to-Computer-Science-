n, m = map(int, input().split())
a = list(map(int, input().split()))
a.sort(reverse=True)
b = [a[i]-a[i-1] for i in range(1, n)]
b.sort()
print(a[0]-a[-1]+sum(b[:m-1]))
