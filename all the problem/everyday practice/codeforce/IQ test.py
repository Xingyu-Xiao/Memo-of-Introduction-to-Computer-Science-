x = int(input())
y = list(map(int, input().split()))


def f(b):
    even = 0
    for m in b:
        if m % 2 == 0:
            even += 1
    if even == 1:
        for m in b:
            if m % 2 == 0:
                s = b.index(m)+1
    else:
        for m in b:
            if m % 2 != 0:
                s = b.index(m)+1
    return s


print(f(y))
