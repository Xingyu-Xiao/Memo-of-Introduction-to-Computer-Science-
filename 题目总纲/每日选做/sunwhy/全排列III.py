n = int(input())
p = [False]*n


def permutate(b, temp):
    if len(temp) == n:
        return [temp]
    else:
        out = []
        for i in range(n):
            if p[i]:
                continue
            else:
                p[i] = True
                out.extend(permutate(b, temp + [b[i]]))
                p[i] = False
        return out


a = list(map(int, input().split()))
a.sort()
output = permutate(a, [])
ans = [tuple(x) for x in output]
tem = set()
for x in ans:
    if x not in tem:
        print(*x)
        tem.add(x)
