def m_ax(x):
    n, a, b, c = x
    dp = [-1]*(n+1)
    dp[0] = 0
    for i in range(min(a, b, c), n+1):
        add_a = dp[i-a] + 1 if i >= a and dp[i-a] >= 0 else -1
        add_b = dp[i-b] + 1 if i >= b and dp[i-b] >= 0 else -1
        add_c = dp[i-c] + 1 if i >= c and dp[i-c] >= 0 else -1
        dp[i] = max(add_a, add_b, add_c)
    return dp[-1]


print(m_ax(map(int, input().split())))
