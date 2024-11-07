n = int(input())
s = [list(map(int, input().split())) for _ in range(n)]
dp = [[0 for _ in range(i+1)] for i in range(n)]
dp[0][0] = s[0][0]
for i in range(1, n):
    for j in range(i+1):
        if j == 0:
            dp[i][j] = dp[i-1][j] + s[i][j]
        elif j == i:
            dp[i][j] = dp[i-1][j-1] + s[i][j]
        else:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-1]) + s[i][j]
ans = [x for x in dp[-1]]
print(max(ans))
