from functools import lru_cache
r, c = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(r)]
dire = [(-1, 0), (1, 0), (0, -1), (0, 1)]
out = []


@lru_cache(maxsize=None)
def dfs(x, y):
    ans = []
    p = True
    for dx, dy in dire:
        nx, ny = x + dx, y + dy
        if 0 <= nx < r and 0 <= ny < c and arr[nx][ny] < arr[x][y]:
            ans.append(dfs(nx, ny)+1)
            p = False
    if p:
        return 1
    return max(ans)


for i in range(r):
    for j in range(c):
        out.append(dfs(i, j))
print(max(out))
