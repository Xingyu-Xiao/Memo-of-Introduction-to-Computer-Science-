a = int(input())


def f():
    s = []
    for i in range(3*a):
        s.append(input())
    return s


b = f()
for i in range(a):
    q = b[3*i:3*i+3]
    n = sum(map(int, q[1].split()))
    nn = sum(map(int, q[2].split()))
    m = int(q[0])*min(map(int, q[2].split()))
    mm = int(q[0])*min(map(int, q[1].split()))
    if n+m < nn+mm:
        print(n+m)
    else:
        print(nn+mm)
