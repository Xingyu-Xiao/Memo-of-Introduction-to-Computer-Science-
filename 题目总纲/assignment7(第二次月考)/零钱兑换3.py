n, m = map(int, input().split())
s = list(map(int, input().split()))
dp = [m+1]*(m+1)
dp[0] = 0
for i in range(1, m+1):
    add = []
    for x in s:
        add_x = dp[i-x] + 1 if (i-x >= 0 and dp[i-x] < m+1) else m+1
        add.append(add_x)
    dp[i] = min(add)
if dp[-1] != m+1:
    print(dp[-1])
else:
    print(-1)
