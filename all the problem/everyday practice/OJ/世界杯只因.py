n = int(input())
a = list(map(int, input().split()))
s = [(max(i-a[i], 0), -min(i+a[i], n-1)) for i in range(n)]
s.sort()
last = -1
new = -1
ans = 0
for st, en in s:
    en = -en
    if st <= last:
        new = max(en, new)
    else:
        ans += 1
        if st == last+1:
            last = max(en, new)
        else:
            last = new
        new = last
print(ans)
