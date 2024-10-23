import bisect
n = int(input())
s = list(map(int, input().split()))
sum_s = sum(s)
a = [0]*n
a[0] = s[0]
for i in range(1, n):
    a[i] = a[i-1] + s[i]
if sum_s % 3 != 0:
    print(0)
else:
    out = 0
    p_1 = []
    p_2 = []
    for i, x in enumerate(a):
        if x == sum_s//3:
            p_1.append(i)
        if x == 2*sum_s//3 and i != n-1:
            p_2.append(i)
    for y in p_1:
        k = bisect.bisect_right(p_2, y)
        out += len(p_2) - k
    print(out)
