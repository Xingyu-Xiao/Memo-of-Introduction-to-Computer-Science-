from functools import lru_cache


@lru_cache(maxsize=None)
def hanoi3(k):
    if k == 1:
        return 1
    return 2*hanoi3(k-1) + 1


dp = [0]*13
dp[1] = 1
for i in range(2, 13):
    temp = [2*dp[i-k] + hanoi3(k) for k in range(1, 13)]
    dp[i] = min(temp)


for n in range(1, 13):
    print(dp[n])
