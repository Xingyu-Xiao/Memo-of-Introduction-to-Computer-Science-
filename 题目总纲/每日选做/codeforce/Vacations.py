n = int(input())
a = list(map(int, input().split()))
dp = [0 for _ in range(n)]
dp[0] = 1 if a[0] == 0 else 0
if n == 1:
    print(dp[0])
else:
    if a[0] == 0:
        last = 0
    elif a[0] == 1:
        last = 1
    elif a[0] == 2:
        last = 2
    else:
        last = 0
    i = 1
    while i < n:
        if a[i] == 0:
            last = 0
            dp[i] = dp[i-1] + 1
        elif a[i] == 1:
            if last == 1:
                dp[i] = dp[i-1] + 1
                last = 0
            else:
                last = 1
                dp[i] = dp[i-1]
        elif a[i] == 2:
            if last == 2:
                dp[i] = dp[i-1] + 1
                last = 0
            else:
                dp[i] = dp[i-1]
                last = 2
        else:
            if last == 1:
                last = 2
            elif last == 2:
                last = 1
            else:
                last = 0
            dp[i] = dp[i-1]
        i += 1
    print(dp[-1])

