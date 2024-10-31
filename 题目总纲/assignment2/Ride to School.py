import math
ss = []
while True:
    n = int(input())
    if n == 0:
        break
    else:
        s = []
        for i in range(n):
            a, b = map(int, input().split())
            s.append([a, b])
        ss.append(s)
for s in ss:
    time = [(4500*3.6/x[0]+x[1]) for x in s if x[1] >= 0]
    print(math.ceil(min(time)))
