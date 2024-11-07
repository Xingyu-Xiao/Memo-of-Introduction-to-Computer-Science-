n = int(input())
s = [tuple(map(int, input().split())) for _ in range(n)]
s.sort(key=lambda x: (x[1], -x[0]))
ans = 1
last = s[0][1]
for x in s[1:]:
    if x[0] > last:
        ans += 1
        last = x[1]
    else:
        continue
print(ans)
