n, d = map(int, input().split())
a = [int(input()) for _ in range(n)]
while a:
    s_max = []
    s__max = 0
    s_min = []
    s__min = 10 ** 9 + 1
    for x in a:
        s__max = max([s__max, x])
        s__min = min([s__min, x])
        s_max.append(s__max)
        s_min.append(s__min)
    free = []
    unfree = []
    for index, x in enumerate(a):
        if s_max[index]-x <= d and x-s_min[index] <= d:
            free.append(x)
        else:
            unfree.append(x)
    free.sort()
    print('\n'.join(map(str, free)))
    a = unfree
