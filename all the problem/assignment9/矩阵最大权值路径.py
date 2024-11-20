n, m = map(int, input().split())
s = [list(map(int, input().split())) for _ in range(n)]
visited = [[True for _ in range(m)] for _ in range(n)]
max_path = []
max_sum = float('-inf')
visited[0][0] = False


def dfs(start, c_sum, c_path):
    global max_path, max_sum
    if start == (n-1, m-1):
        if c_sum > max_sum:
            max_sum = c_sum
            max_path = c_path.copy()
        return
    for dx, dy in ((-1, 0), (1, 0), (0, -1), (0, 1)):
        nx, ny = start[0] + dx, start[1] + dy
        if 0 <= nx < n and 0 <= ny < m and visited[nx][ny]:
            visited[nx][ny] = False
            c_path.append((nx, ny))
            dfs((nx, ny), c_sum + s[nx][ny], c_path)
            visited[nx][ny] = True
            c_path.pop()


dfs((0, 0), s[0][0], [(0, 0)])
for path in max_path:
    print(path[0]+1, path[1]+1)
