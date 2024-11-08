T, n = map(int, input().split())
tw = [tuple(map(int, input().split())) for _ in range(n)]
dp = [-float('inf')]*(T+1)
dp[0] = 0
for t, w in tw:
    for i in range(T, t-1, -1):
        dp[i] = max(dp[i], dp[i-t]+w)
if dp[-1] == -float('inf'):
    print(-1)
else:
    print(dp[-1])
