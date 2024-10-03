a = int(input())
if a % 2 == 0 and a > 0:
    if a % 4 == 0:
        print(a//4, a//2)
    else:
        print(a//4+1, a//2)
else:
    print(0, 0)

