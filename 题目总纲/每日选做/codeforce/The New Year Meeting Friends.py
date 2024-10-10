a = list(map(int, input().split()))
a.sort()
s = 0
for i in range(0, len(a)//2):
    s += (a[-i-1] - a[i])
print(s)
