import math
i = 0
while True:
    try:
        n, d = map(int, input().split())
    except ValueError:
        continue
    if (n, d) == (0, 0):
        break
    a = [tuple(map(int, input().split())) for _ in range(n)]
    i += 1
    if any(y[1] for y in a if y[1] > d):
        print(f'Case {i}: -1')
    else:
        s = [(x-math.sqrt(d**2-y**2), x+math.sqrt(d**2-y**2)) for x, y in a]
        s.sort(key=lambda x: x[1])
        last = s[0][1]
        out = 1
        for x in s[1:]:
            if x[0] > last:
                out += 1
                last = x[1]
        print(f'Case {i}: {out}')
