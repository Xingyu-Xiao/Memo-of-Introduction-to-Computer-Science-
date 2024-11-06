t = int(input())
s = list(map(int, input().split()))
s.sort()
i = 0
j = len(s)-1
gap = float('inf')
ans = 0
while i < j:
    m = s[i] + s[j]
    if m == t:
        ans = t
        break
    elif m > t:
        j -= 1
    else:
        i += 1
    if abs(t-m) < gap:
        gap = abs(t-m)
        ans = m
    elif abs(t-m) == gap:
        ans = min(ans, m)
print(ans)
