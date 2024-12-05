import sys
sys.setrecursionlimit(20000)
ss = sys.stdin.read().split()
direction = [(1, 0),(0,1),(-1,0),(0,-1)]


def flood(x, y, s, m, n, v):
    v.add((x, y))
    for dx, dy in direction:
        nx, ny = x + dx, y + dy
        if 0 <= nx < m and 0 <= ny < n and (nx, ny) not in v:
            if s[nx][ny] < s[x][y]:
                s[nx][ny] = s[x][y]
                flood(nx, ny, s, m, n, v)


k = int(ss[0])
idx = 1
for _ in range(k):
    m, n = map(int, ss[idx: idx+2])
    idx += 2
    s = []
    for _ in range(m):
        s.append(list(map(int, ss[idx: idx+n])))
        idx += n
    i, j = map(int, ss[idx: idx+2])
    idx += 2
    origin = s[i-1][j-1]
    p = int(ss[idx])
    idx += 1
    points = []
    for _ in range(p):
        points.append(tuple(map(int, ss[idx: idx+2])))
        idx += 2
    for x, y in points:
        v = set()
        flood(x-1, y-1, s, m, n, v)
    if s[i-1][j-1] == origin:
        print('No')
    else:
        print('Yes')
