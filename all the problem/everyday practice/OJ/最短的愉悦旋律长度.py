n, m = map(int, input().split())
melody = list(map(int, input().split()))
s = set()
ans = 1
for x in melody:
    s.add(x)
    if len(s) == m:
        s.clear()
        ans += 1
print(ans)
