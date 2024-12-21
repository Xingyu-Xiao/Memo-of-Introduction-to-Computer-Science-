import bisect
import math
m, n = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(m)]
s = [list(map(int, input().split())) for _ in range(n*m)]
b = [-sum(x) for x in s]
di = ((0, 1), (1, 0), (0, -1), (-1, 0))
same = 0
for i in range(m):
    for j in range(n):
        p = True
        for dx, dy in di:
            nx, ny = i + dx, j + dy
            if 0 <= nx < m and 0 <= ny < n:
                if s[a[nx][ny]] == s[a[i][j]]:
                    if p:
                        same += 1
                        p = False
b.sort()
rank = math.floor((m*n*0.4))
num = bisect.bisect_left(b, b[rank])
print(same, num)
