a = int(input())


def f():
    s = []
    for i in range(a):
        s.append(input())
    return s


b = f()
for x in b:
    if int(x) % 2 == 0:
        print(int(x)//2-1)
    else:
        print((int(x)-1)//2)
