n, m = map(int, input().split())
a = list(map(int, input().split()))
li = [int(input()) for _ in range(m)]
dp = [0]*n
dp[-1] = 1
s = set()
s.add(a[-1])
for i in range(n-2, -1, -1):
    if a[i] in s:
        dp[i] = dp[i+1]
    else:
        dp[i] = dp[i+1] + 1
        s.add(a[i])
for x in li:
    print(dp[x-1])
