a = int(input())


def f():
    s = []
    for j in range(a):
        s.append(input())
    return s


q = f()
for x in q:
    p = list(x.split())
    for i in range(len(p)):
        p[i] = int(p[i])
    h = p[0]//p[1]
    if p[0] % p[1] != 0:
        print((h+1)*p[1]-p[0])
    else:
        print(0)
