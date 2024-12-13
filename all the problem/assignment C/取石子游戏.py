def g(a, b):
    if a//b >= 2:
        return 'lose'


def f(a, b):
    if a//b >= 2:
        return 'win'
    else:
        if g(b, a-b):
            return g(b, a-b)
        else:
            return f(a-b, 2*b-a)


while True:
    a, b = map(int, input().split())
    if a == 0 and b == 0:
        break
    if a == b:
        print('win')
        continue
    if a < b:
        a, b = b, a
    print(f(a,b))
