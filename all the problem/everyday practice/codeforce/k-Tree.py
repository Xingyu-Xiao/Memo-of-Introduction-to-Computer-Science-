n, k, d = map(int, input().split())
MOD = 1000000007
dp = [[0]*(n+1), [0]*(n+1)]
dp[0][0] = 1
for i in range(1, n+1):
    for j in range(1, k+1):
        if i >= j:
            dp[0][i] = (dp[0][i - j] + dp[0][i]) % MOD
            if j >= d:
                dp[1][i] = (dp[1][i] + dp[0][i-j]) % MOD
            else:
                dp[1][i] = (dp[1][i - j] + dp[1][i]) % MOD
print(dp[1][-1])
