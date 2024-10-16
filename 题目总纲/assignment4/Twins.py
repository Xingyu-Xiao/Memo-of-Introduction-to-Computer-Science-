n = int(input())
a = list(map(int, input().split()))
a = sorted(a, reverse=True)
for i in range(n+1):
    if sum(a[:i]) > sum(a[i:]):
        print(i)
        break
