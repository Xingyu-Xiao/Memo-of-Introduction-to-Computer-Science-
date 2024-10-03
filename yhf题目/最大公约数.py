s = []
while True:
    try:
        a, b = map(int, input().split())
        s.append((a, b))
    except EOFError:
        break
for x in s:
    q = min(x)
    for i in range(q, 0, -1):
        if x[0] % i == x[1] % i == 0:
            print(i)
            break
