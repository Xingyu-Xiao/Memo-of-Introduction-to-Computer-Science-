n, m, k = map(int, input().split())
dp = [[-1]*(m+1) for _ in range(k+1)]
dp[0][m] = n
for i in range(k):
    ball, live = map(int, input().split())
    for p in range(1, m):
        for j in range(i+1, 0, -1):
            if p+live <= m:
                dp[j][p] = max(dp[j][p], dp[j-1][p+live]-ball)
for j in range(k, -1, -1):
    for i in range(m, 0, -1):
        if dp[j][i] >= 0:
            print(j, i)
            exit()

