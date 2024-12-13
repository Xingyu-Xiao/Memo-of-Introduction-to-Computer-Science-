from collections import deque
dire = [(0,1),(1,0),(0,-1),(-1,0)]


def bfs(i, j):
    queue = deque([(i, j, 0)])
    visited = {(i, j, 0)}
    while queue:
        x, y, n = queue.popleft()
        for dx, dy in dire:
            nx, ny = x + dx, y + dy
            if 0 <= nx < r and 0 <= ny < c and (nx, ny, (n+1) % k) not in visited:
                if maze[nx][ny] == 'E':
                    return n+1
                if (n+1) % k == 0 or maze[nx][ny] != '#':
                    queue.append((nx, ny, n+1))
                    visited.add((nx, ny, (n+1) % k))
    return 'Oop!'


t = int(input())
for _ in range(t):
    r, c, k = map(int, input().split())
    maze = [input() for _ in range(r)]
    p = False
    for i in range(r):
        for j in range(c):
            if maze[i][j] == 'S':
                print(bfs(i, j))
                p = True
                break
        if p:
            break
    p = False
