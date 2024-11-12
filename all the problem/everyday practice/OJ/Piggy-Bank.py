t = int(input())
for _ in range(t):
    E, F = map(int, input().split())
    N = int(input())
    pw = [tuple(map(int, input().split())) for _ in range(N)]
    dp = [float('inf')]*(-E+F+1)
    dp[0] = 0
    for p, w in pw:
        for i in range(w, F - E + 1):
            dp[i] = min(dp[i-w] + p, dp[i])
    if dp[-1] == float('inf'):
        print('This is impossible.')
    else:
        print(f'The minimum amount of money in the piggy-bank is {dp[-1]}.')
