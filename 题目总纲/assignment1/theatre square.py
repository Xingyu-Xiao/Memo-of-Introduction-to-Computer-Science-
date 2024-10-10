x, y, z = input().split()
x, y, z = int(x), int(y), int(z)
if x % z == 0:
    a = x//z
    if y % z == 0:
        b = y//z
        print(a * b)
    else:
        b = y // z + 1
        print(a * b)
if x % z != 0:
    a = x // z+1
    if y % z != 0:
        b = y//z+1
        print(a * b)
    else:
        b = y // z
        print(a * b)
