n = int(input())
if n == 1:
    print(1)
else:
    dp = [0]*n
    dp[0] = 1
    for i in range(1, n):
        dp[i] = sum(dp[:i]) + 1
    print(dp[-1])
    