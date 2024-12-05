from sys import stdin
MOD = 10 ** 9 + 7
data = stdin.readlines()
ans = []
result = [0]*100001
t, k = map(int, data[0].strip().split())
dp = [0]*100001
for i in range(k):
    dp[i] = 1
for i in range(k, 100001):
    dp[i] = (dp[i-1] + dp[i-k]) % MOD
for i in range(100001):
    result[i] = result[i-1] + dp[i]
for line in data[1:]:
    a, b = map(int, line.strip().split())
    ans.append((result[b]-result[a-1]) % MOD)
print('\n'.join(map(str, ans)))
