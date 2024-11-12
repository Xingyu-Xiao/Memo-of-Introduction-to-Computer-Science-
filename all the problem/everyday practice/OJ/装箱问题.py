import math
finish = [0]*6
s = []
while True:
    a = list(map(int, input().split()))
    if a == finish:
        break
    else:
        s.append(a)
for x in s:
    n = sum(x[3:]) + math.ceil(x[2]/4)
    n_3 = x[2] % 4
    n_1 = x[0]
    n_2 = x[1]
    space = 11*x[4]
    if n_2 > x[3]*5:
        n_2 -= x[3]*5
        if n_3 == 1:
            remain = 5
            space += 7
        elif n_3 == 2:
            remain = 3
            space += 6
        elif n_3 == 3:
            remain = 1
            space += 5
        else:
            remain = 0
        if n_2 >= remain:
            n_2 -= remain
            n += math.ceil(n_2/9)
            if n_2 % 9 != 0:
                space += (36-4*(n_2 % 9))
            if n_1 <= space:
                print(n)
            else:
                print(n + math.ceil((n_1 - space) / 36))
        else:
            space += 4*(remain-n_2)
            if n_1 <= space:
                print(n)
            else:
                print(n + math.ceil((n_1 - space) / 36))
    else:
        if n_3 > 0:
            space += 4*(x[3]*5-n_2)+(36-n_3*9)
        else:
            space += 4*(x[3]*5-n_2)
        if n_1 <= space:
            print(n)
        else:
            print(n+math.ceil((n_1-space)/36))
