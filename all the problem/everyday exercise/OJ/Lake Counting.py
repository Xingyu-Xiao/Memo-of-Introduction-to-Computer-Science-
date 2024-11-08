import sys
sys.setrecursionlimit(20000)


def count_pond(n, m, field):
    directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    count = 0

    def dfs(x, y):
        if x < 0 or y < 0 or x >= n or y >= m:
            return
        if field[x][y] != 'W':
            return
        field[x][y] = '.'
        for dx, dy in directions:
            dfs(x + dx, y + dy)

    for i in range(n):
        for j in range(m):
            if field[i][j] == 'W':
                dfs(i, j)
                count += 1
    return count


n, m = map(int, input().split())
field = [list(input()) for _ in range(n)]
print(count_pond(n, m, field))
