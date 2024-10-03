n, m = map(int, input().split())
s = []
for i in range(n):
    s.append(list(map(int, input().split())))
ss = []
for x in s:
    for y in x[1:]:
        ss.append(y)
ss = set(ss)
p = 0
for i in range(1, m+1):
    if i in ss:
        pass
    else:
        print('NO')
        p = 1
        break
if p == 0:
    print('YES')
