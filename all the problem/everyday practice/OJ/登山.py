n = int(input())
*h, = map(int, input().split())
rh = list(reversed(h))
dp = [0]*n
rdp = [0 for _ in range(n)]
dp[0] = rdp[0] = 1
for i in range(1, n):
    dp[i] = max(dp[j]+1 if h[j] < h[i] else 1 for j in range(i))
    rdp[i] = max(rdp[j]+1 if rh[j] < rh[i] else 1 for j in range(i))
print(max(dp[i]+rdp[n-i-1] for i in range(n))-1)
