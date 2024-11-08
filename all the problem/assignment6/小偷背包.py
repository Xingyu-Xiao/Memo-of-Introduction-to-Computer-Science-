n, b = map(int, input().split())
price = list(map(int, input().split()))
weight = list(map(int, input().split()))
dp = [0]*(b+1)
for i in range(n):
    for j in range(b, weight[i]-1, -1):
        dp[j] = max(dp[j], price[i]+dp[j-weight[i]])
print(dp[-1])
