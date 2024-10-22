n = int(input())
a = [tuple(map(int, input().split())) for _ in range(n)]
if n > 1:
    out = 2
    last = a[0][0]
    for i in range(1, n-1):
        x, h = a[i]
        if x-h > last:
            out += 1
            last = x
        elif x+h < a[i+1][0]:
            out += 1
            last = x+h
        else:
            last = x
    print(out)
else:
    print(1)
'''
n = int(input())
a = [tuple(map(int, input().split())) for _ in range(n)]
if n > 1:
    out = 2
    p = True
    for i in range(1, n-1):
        if a[i][0] - a[i-1][0] > a[i][1]:
            if p:
                out += 1
            else:
                if a[i][0] - a[i-1][0] > a[i][1] + a[i-1][1]:
                    out += 1
                    p = True
                else:
                    if -a[i][0] + a[i + 1][0] > a[i][1]:
                        out += 1
                        p = False
                    else:
                        p = True
        else:
            if -a[i][0] + a[i+1][0] > a[i][1]:
                out += 1
                p = False
            else:
                p = True
    print(out)
else:
    print(1)
'''