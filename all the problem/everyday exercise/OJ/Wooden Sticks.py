from bisect import bisect_right
from collections import deque
t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    w = [a[i] for i in range(1, 2*n, 2)]
    li = [a[i] for i in range(0, 2*n, 2)]
    lw = list(zip(li, w))
    lw.sort()
    lis = deque([])
    for i in range(n):
        index = bisect_right(lis, lw[i][1])
        if index == 0:
            lis.appendleft(lw[i][1])
        else:
            lis[index-1] = lw[i][1]
    print(len(lis))
