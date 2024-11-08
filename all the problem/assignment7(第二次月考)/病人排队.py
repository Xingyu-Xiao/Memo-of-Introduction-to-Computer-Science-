n = int(input())
s = [[_] + list(input().split()) for _ in range(n)]
s_60 = [x for x in s if int(x[2]) >= 60]
ss = [x for x in s if int(x[2]) < 60]
s_60.sort(key=lambda x: (-int(x[2]), x[0]))
ans = s_60 + ss
for y in ans:
    print(y[1])