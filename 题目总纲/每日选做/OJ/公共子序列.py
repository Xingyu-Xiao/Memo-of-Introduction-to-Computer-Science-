while 1:
    try:
        a, b = input().split()
        n_a = len(a)
        n_b = len(b)
        dp = [[0 for _ in range(n_b+1)] for _ in range(n_a+1)]
        for i in range(1, n_a+1):
            for j in range(1, n_b+1):
                if a[i-1] == b[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        print(dp[-1][-1])
    except EOFError:
        break
