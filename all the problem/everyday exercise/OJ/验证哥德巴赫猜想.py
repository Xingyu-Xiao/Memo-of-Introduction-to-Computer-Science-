a = int(input())
if a < 6 or a % 2 != 0:
    print('Error!')
else:
    s = [2, 3, 5, 7]
    for i in range(11, 2000, 6):
        q = 0
        for x in s:
            if i % x == 0:
                q = 1
        if q == 0:
            s.append(i)
        q = 0
        for x in s:
            if (i+2) % x == 0:
                q = 1
        if q == 0:
            s.append(i+2)
    for y in s:
        if (a - y) in s and (a - y) >= y:
            print(f'{a}={y}+{a-y}')

