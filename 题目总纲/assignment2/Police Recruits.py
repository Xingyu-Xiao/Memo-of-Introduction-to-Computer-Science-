b = int(input())
a = list(map(int, input().split()))


def f(n, m):
    x = 0
    y = 0
    for o in m:
        if o < 0:
            if y > 0:
                y += o
            else:
                x -= o
        else:
            y += o
    return x


print(f(b, a))
