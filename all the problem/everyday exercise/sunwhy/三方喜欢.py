n, q = map(int, input().split())
a = [tuple(map(int, input().split())) for _ in range(q)]
p = False
for x in a:
    for y in a:
        if x[1] == y[0]:
            for z in a:
                if y[1] == z[0] and z[1] == x[0]:
                    print('Yes')
                    p = True
                    break
            if p:
                break
    if p:
        break
else:
    print('No')
