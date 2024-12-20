from functools import cmp_to_key
m = int(input())
n = int(input())
s = input().split()


def cmp(a, b):
    if a+b > b+a:
        return 1
    elif a+b < b+a:
        return -1
    else:
        return 0


s.sort(key=cmp_to_key(cmp))
dp = [['' for i in range(m+1)] for j in range(n+1)]
for i in range(1, n+1):
    for j in range(1, m+1):
        if len(s[i-1]) > j:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = str(max(int(dp[i-1][j]) if dp[i-1][j] else 0, int(s[i-1]+dp[i-1][j-len(s[i-1])])))
print(dp[-1][-1])
