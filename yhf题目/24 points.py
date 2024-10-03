a = int(input())
s = []
for i in range(a):
    x = list(map(int, input().split()))
    s.append(x)
for b in s:
    if sum(b) < 24:
        print('NO')
    elif sum(b) == 24:
        print('YES')
    else:
        b.sort(reverse=True)
        if b[0] - sum(b[1:]) > 24:
            print('NO')
        elif b[0] - sum(b[1:]) == 24:
            print('YES')
        else:
            if b[0] + b[1] - b[2] - b[3] == 24 or b[0] - b[1] + b[2] - b[3] == 24 or b[0] - b[1] - b[2] + b[3] == 24 or b[1] - b[0] + b[2] - b[3] == 24:
                print('YES')
            elif b[0] + b[1] - b[2] + b[3] == 24 or b[0] + b[1] + b[2] - b[3] == 24 or b[0] - b[1] + b[2] + b[3] == 24 or sum(b[1:]) - b[0] == 24:
                print('YES')
            else:
                print('NO')
