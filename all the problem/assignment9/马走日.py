direction = ((1, 2), (1, -2), (-1, 2), (-1, -2), (2, -1), (2, 1), (-2, 1), (-2, -1))


def solve(n, m, x, y):
    ans = 0
    visited = [[False for _ in range(m)] for _ in range(n)]
    visited[x][y] = True

    def dfs(start):
        nonlocal ans
        nx_ny = [(start[0]+dx, start[1]+dy) for dx, dy in direction if 0 <= start[0]+dx < n and 0 <= start[1]+dy < m]
        if not any(not visited[nx][ny] for nx, ny in nx_ny):
            for i in range(n):
                for j in range(m):
                    if not visited[i][j]:
                        return
            ans += 1
            return
        for dx, dy in direction:
            nx, ny = start[0] + dx, start[1] + dy
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
                visited[nx][ny] = True
                dfs((nx, ny))
                visited[nx][ny] = False
    dfs((x, y))
    return ans


t = int(input())
for _ in range(t):
    n, m, x, y = map(int, input().split())
    print(solve(n, m, x, y))
