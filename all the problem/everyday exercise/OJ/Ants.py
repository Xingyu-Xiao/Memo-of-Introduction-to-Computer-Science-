a = int(input())
for i in range(a):
    L, n = map(int, input().split())
    s = list(map(int, input().split()))
    ss = [min([L-x, x]) for x in s]
    sss = [max([L-x, x])for x in s]
    min_time = max(ss)
    max_time = max(sss)
    print(min_time, max_time)
