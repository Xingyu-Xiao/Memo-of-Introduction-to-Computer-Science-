import sys
n = int(input())
a = list(map(int, input().split()))
m = max(a)
s = [0]*(m+1)
for x in a:
    s[x] += 1
if m == 1:
    print(s[1])
    sys.exit()
if m == 2:
    print(max(s[2], 2*s[1]))
    sys.exit()
dp = [0]*(m+1)
dp[-1] = m*s[-1]
dp[-2] = max((m-1)*s[-2], m*s[-1])
for i in range(m-2, 0, -1):
    dp[i] = max(dp[i+1], dp[i+2] + i*s[i])
print(dp[1])
