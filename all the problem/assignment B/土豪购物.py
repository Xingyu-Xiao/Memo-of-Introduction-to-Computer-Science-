s = list(map(int, input().split(',')))
dp1 = [0]*len(s)
dp2 = [0]*len(s)
dp1[0] = s[0]
dp2[0] = s[0]
for i in range(1, len(s)):
    dp1[i] = max(s[i], s[i]+dp1[i-1])
    dp2[i] = max(dp1[i], dp1[i-1], dp2[i-1]+s[i], s[i])
print(max(dp2))
