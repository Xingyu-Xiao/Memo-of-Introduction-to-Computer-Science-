a = int(input())


def f():
    p = []
    for i in range(1, a+1):
        p.append(input())
    return p


b = f()
for x in b:
    s, m, n = map(int, x.split())
    if s + m == n or s == m + n or m == s + n:
        print('yes')
    else:
        print('NO')
