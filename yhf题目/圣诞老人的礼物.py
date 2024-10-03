n, m = map(int, input().split())
s = [list(map(int, input().split())) for _ in range(n)]
s.sort(key=lambda o: o[0]/o[1], reverse=True)
value = 0
p = 1
for x in s:
    if m > x[1]:
        m -= x[1]
        value += x[0]
        if x == s[-1]:
            p = 0
    else:
        y = x
        break
if p == 1:
    value += (m/y[1]*y[0])
print(f'{value:.1f}')
