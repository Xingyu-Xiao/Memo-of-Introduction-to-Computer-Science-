def num(n):
    if n == 1:
        return 1
    else:
        return 2*num(n-1) + 1


def move_one(ori, aim):
    print(f'{ori}->{aim}')


def move(n, a, b, c):
    if n == 1:
        move_one(a, c)
    else:
        move(n-1, a, c, b)
        move_one(a, c)
        move(n-1, b, a, c)


k = int(input())
print(num(k))
move(k, 'A', 'B', 'C')
