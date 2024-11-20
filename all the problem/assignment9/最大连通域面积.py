from collections import deque


def bfs(s, n, m, i, j):
    queue = deque([(i, j)])
    con = 0
    while queue:
        x, y = queue.popleft()
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                if 0 <= x + dx < n and 0 <= y + dy < m:
                    if s[x + dx][y + dy] == 'W':
                        queue.append((x + dx, y + dy))
                        con += 1
                        s[x + dx][y + dy] = '.'
    return con


t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    s = [list(input()) for _ in range(n)]
    ans = 0
    for i in range(n):
        for j in range(m):
            if s[i][j] == 'W':
                ans = max(ans, bfs(s, n, m, i, j))
    print(ans)
