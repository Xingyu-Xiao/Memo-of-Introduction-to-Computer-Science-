n, m = map(int, input().split())
dp = [0]*(n+2)
dp[0] = 1
for i in range(n+2):
    for j in range(m):
        dp[i] += dp[i-j-1] if i-j-1 >= 0 else 0
print(dp[-1])
