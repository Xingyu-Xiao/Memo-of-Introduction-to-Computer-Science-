n, m = map(int, input().split())
a = [tuple(map(int, input().split())) for _ in range(n)]
s = []
for x in a:
    qvjian = []
    for start in range(max(0, x[0]-x[1]+1), min(x[0]+1, m)):
        end = start + x[1]
        if end <= m:
            qvjian.append((start, end))
    s.extend(qvjian)
s.sort(key=lambda x: (x[1], x[0]))
ans = 0
last = 0
for st, en in s:
    if st >= last:
        ans += 1
        last = en
print(ans)
