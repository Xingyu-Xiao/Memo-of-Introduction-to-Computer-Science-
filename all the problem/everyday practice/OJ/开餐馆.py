import bisect


def solve(n, k, m, p):
    dp = [0]*n
    dp[0] = p[0]
    for i in range(1, n):
        index = bisect.bisect_left(m, m[i]-k)
        if index == i:
            dp[i] = dp[i-1] + p[i]
        else:
            dp[i] = max(dp[i-1], dp[index-1]+p[i])
    return dp[-1]


t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    m = list(map(int, input().split()))
    p = list(map(int, input().split()))
    print(solve(n, k, m, p))
