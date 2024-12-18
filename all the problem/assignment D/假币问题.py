n = int(input())
for _ in range(n):
    lis = {'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L'}
    a = list(input().split())
    b = list(input().split())
    c = list(input().split())
    if a[2] == 'even':
        lis.difference_update(set(a[0]+a[1]))
    if b[2] == 'even':
        lis.difference_update(set(b[0]+b[1]))
    if c[2] == 'even':
        lis.difference_update(set(c[0]+c[1]))
    if a[2] != 'even':
        s = set(a[0]+a[1])
        lis.intersection_update(s)
    if b[2] != 'even':
        s = set(b[0] + b[1])
        lis.intersection_update(s)
    if c[2] != 'even':
        s = set(c[0]+c[1])
        lis.intersection_update(s)
    for ans in lis:
        p = set()
        if a[2] != 'even':
            if a[2] == 'up':
                if ans in a[1]:
                    p.add('light')
                else:
                    p.add('heavy')
            else:
                if ans in a[1]:
                    p.add('heavy')
                else:
                    p.add('light')
        if b[2] != 'even':
            if b[2] == 'up':
                if ans in b[1]:
                    p.add('light')
                else:
                    p.add('heavy')
            else:
                if ans in b[1]:
                    p.add('heavy')
                else:
                    p.add('light')
        if c[2] != 'even':
            if c[2] == 'up':
                if ans in c[1]:
                    p.add('light')
                else:
                    p.add('heavy')
            else:
                if ans in c[1]:
                    p.add('heavy')
                else:
                    p.add('light')
        if len(p) == 1:
            an = ans
            pp = p.pop()
    print(f'{an} is the counterfeit coin and it is {pp}.')
