n, t = map(int, input().split())
a = list(map(int, input().split()))
sum_a = sum(a)
if sum(a) < t:
    print(0)
else:
    dp = [[0]*(sum_a+1) for i in range(n)]
    for i in range(n):
        for j in range(sum_a+1):
            if a[i] > j:
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = max(dp[i-1][j], dp[i-1][j-a[i]]+a[i])
    for j in range(t, sum_a+1):
        if dp[-1][j] >= t:
            print(dp[-1][j])
            break
