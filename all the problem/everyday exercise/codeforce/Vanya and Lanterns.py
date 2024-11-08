n, l = map(int, input().split())
a = list(map(int, input().split()))
a.sort()
s = [a[0]-0] + [(a[i+1] - a[i])/2 for i in range(n-1)] + [l - a[n-1]]
print(max(s))

