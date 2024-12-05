a = list(map(int, input().split()))
ans = 0
s = [(x, i) for i, x in enumerate(a)]
s.sort()
for i in range(len(s)):
    for j in range(len(s)-1,i,-1):
        if s[j][1] > s[i][1]:
            ans = max(ans,s[j][0] - s[i][0])
            break
print(ans)
