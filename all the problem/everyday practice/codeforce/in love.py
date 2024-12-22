from collections import Counter
n = int(input())
start_li, end_li = Counter([]), Counter([])
ma = 1
mi = 10**9
for _ in range(n):
    add = input().split()
    start = int(add[1])
    end = int(add[2])
    if add[0] == '+':
        start_li[start] += 1
        end_li[end] += 1
        ma = max(ma, start)
        mi = min(mi, end)
    else:
        start_li[start] -= 1
        end_li[end] -= 1
        if start_li[start] == 0:
            del start_li[start]
            if start == ma:
                ma = max(start_li.keys(), default=1)
        if end_li[end] == 0:
            del end_li[end]
            if end == mi:
                mi = min(end_li.keys(), default=10**9)
    if mi < ma:
        print('yes')
    else:
        print('no')
