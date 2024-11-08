p = [False]*9


def f(n, tem=[]):
    if len(tem) == n:
        return [tem]
    else:
        out = []
        for i in range(1, n+1):
            if p[i]:
                continue
            else:
                p[i] = True
                out.extend(f(n, tem+[i]))
                p[i] = False
        return out


for x in f(int(input())):
    print(*x)
