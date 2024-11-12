n, q = map(int, input().split())
a = [tuple(map(int, input().split())) for _ in range(q)]
aa = [(x[1], x[0]) for x in a] + a
if len(aa) == len(set(aa)):
    print('No')
else:
    print('Yes')
