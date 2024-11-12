m = int(input())
n = int(input())
dp = [[0 for _ in range(n+1)] for _ in range(m+1)]
dp[1][0] = 1
for i in range(1, m+1):
    for j in range(1, n+1):
        dp[i][j] = dp[i-1][j] + dp[i][j-1]
print(dp[-1][-1])
