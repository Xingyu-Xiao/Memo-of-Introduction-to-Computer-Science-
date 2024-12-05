from collections import deque
n = int(input())
s = [list(input()) for _ in range(n)]
dire = [(1, 0), (-1, 0), (0, 1), (0, -1)]


def f():
    a = set()
    for i in range(n):
        for j in range(n):
            if s[i][j] == '1':
                s[i][j] = '-1'
                queue = deque([(i, j)])
                while queue:
                    x, y = queue.popleft()
                    for dx, dy in dire:
                        nx, ny = x + dx, y + dy
                        if 0 <= nx < n and 0 <= ny < n:
                            if s[nx][ny] == '1':
                                queue.append((nx, ny))
                                s[nx][ny] = '-1'
                            elif s[nx][ny] == '0':
                                a.add((x, y))
                return a


ans = float('inf')
island1 = f()
island2 = f()
for x in island1:
    for y in island2:
        i, j = x
        k, p = y
        ans = min(ans, abs(i-k)+abs(j-p)-1)
print(ans)
