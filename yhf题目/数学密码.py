a = int(input())
s = [6, 7, 8, 9, 10, 11, 13, 15, 17, 19, 23, 25]
b = 0
for x in s:
    if a % x == 0:
        print(a//x)
        b = 1
        break
if b == 0:
    for i in range(29, a//2+1, 6):
        if a % i == 0 or a % (i+2) == 0:
            if a % i == 0:
                print(a//i)
                b = 1
                break
            elif a % (i+2) == 0:
                print(a//(i+2))
                b = 1
                break
if b == 0:
    print(1)
