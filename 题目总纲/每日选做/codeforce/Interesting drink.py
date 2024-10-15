n = int(input())
x = list(map(lambda y: (int(y), -1), input().split()))
q = int(input())
m = [(int(input()), _) for _ in range(q)]
xm = x+m
xm.sort()
out = []
i = 0
for xx in xm:
    if xx[1] >= 0:
        out.append((xx[1], i))
    else:
        i += 1
out.sort()
for z in out:
    print(z[1])
