def divide(x):
    dp = [[0 for _ in range(x+1)] for _ in range(x+1)]
    for i in range(1, x+1):
        dp[1][i] = 1
        dp[i][1] = 1
    for i in range(2, x+1):
        for j in range(2, x+1):
            if i < j:
                dp[i][j] = dp[i][i]
            elif i == j:
                dp[i][j] = dp[i][j-1] + 1
            else:
                dp[i][j] = dp[i][j-1] + dp[i-j][j]
    return dp[x][x]


while True:
    try:
        a = int(input())
        print(divide(a))
    except EOFError:
        break
