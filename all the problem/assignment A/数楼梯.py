n = int(input())
dp = [0]*n
if n > 2:
    dp[0] = 1
    dp[1] = 2
    for i in range(2, n):
        dp[i] = dp[i-1] + dp[i-2]
    print(dp[-1])
if (n == 1) or (n == 2):
    print(n)
