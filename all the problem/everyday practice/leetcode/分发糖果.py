def candy(ratings):
    n = len(ratings)
    dp = [1]*n
    for i in range(1, n):
        if ratings[i] > ratings[i-1]:
            dp[i] = dp[i-1] + 1
    for j in range(n-2, -1, -1):
        if ratings[j] > ratings[j+1]:
            dp[j] = max(dp[j], dp[j+1]+1)
    return sum(dp)

