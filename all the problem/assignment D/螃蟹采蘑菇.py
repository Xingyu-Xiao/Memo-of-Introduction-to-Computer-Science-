from collections import deque

n = int(input())
maze = [list(map(int, input().split())) for _ in range(n)]
dire = ((0, -1), (1, 0), (0, 1), (-1, 0))


def find():
    for i in range(n):
        for j in range(n-1):
            if maze[i][j] == 5 and maze[i][j+1] == 5:
                return ((i, j), True)
    for i in range(n-1):
        for j in range(n):
            if maze[i][j] == 5 and maze[i+1][j] == 5:
                return ((i, j), False)


def bfs1(start):
    queue = deque([start])
    visited = set()
    visited.add(start)
    while queue:
        x, y = queue.popleft()
        for dx, dy in dire:
            nx, ny = x + dx, y + dy
            if (0 <= nx < n) and (0 <= ny < n-1) and (maze[nx][ny] != 1) and ((nx, ny) not in visited) and (maze[nx][ny+1] != 1):
                if maze[nx][ny] == 9 or maze[nx][ny+1] == 9:
                    return 'yes'
                queue.append((nx, ny))
                visited.add((nx, ny))
    return 'no'


def bfs2(start):
    queue = deque([start])
    visited = set()
    visited.add(start)
    while queue:
        x, y = queue.popleft()
        for dx, dy in dire:
            nx, ny = x + dx, y + dy
            if (0 <= nx < n-1) and (0 <= ny < n) and (maze[nx][ny] != 1) and ((nx, ny) not in visited) and (
                    maze[nx+1][ny] != 1):
                if maze[nx][ny] == 9 or maze[nx+1][ny] == 9:
                    return 'yes'
                queue.append((nx, ny))
                visited.add((nx, ny))
    return 'no'


st = find()
if st[1]:
    print(bfs1(st[0]))
else:
    print(bfs2(st[0]))
