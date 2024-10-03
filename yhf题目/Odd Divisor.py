b = int(input())


def h():
    s = []
    for i in range(b):
        s.append(int(input()))
    return s


p = h()
for a in p:
    while a % 2 == 0:
        a = a//2
    if a == 1:
        print('NO')
    else:
        print('YES')
