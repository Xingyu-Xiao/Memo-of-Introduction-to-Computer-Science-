n = int(input())
a = list(map(int, input().split()))
s = {}
for x in a:
    if x in s:
        s[x] += 1
    else:
        s[x] = 1
ss = s.values()
print(max(ss))
