import heapq
dire = [(0,1),(-1,0),(0,-1),(1,0)]
m, n, p = map(int, input().split())
graph = [input().split() for _ in range(m)]
for i in range(m):
    for j in range(n):
        try:
            graph[i][j] = int(graph[i][j])
        except ValueError:
            continue


def dijkstra(start, end):
    if graph[start[0]][start[1]] == '#':
        return float('inf')
    dist = {(i, j): float('inf') for i in range(m) for j in range(n)}
    queue = [(0, start)]
    dist[start] = 0
    while queue:
        cur_dist, node = heapq.heappop(queue)
        x, y = node
        if cur_dist < dist[node]:
            continue
        for dx, dy in dire:
            nx, ny = x + dx, y + dy
            if 0 <= nx < m and 0 <= ny < n:
                if graph[nx][ny] != '#':
                    new_dist = cur_dist + abs(graph[nx][ny]-graph[x][y])
                    if new_dist < dist[(nx, ny)]:
                        dist[(nx, ny)] = new_dist
                        heapq.heappush(queue, (new_dist, (nx, ny)))
    return dist[end]


for _ in range(p):
    s = list(map(int, input().split()))
    ans = dijkstra((s[0], s[1]), (s[2], s[3]))
    if ans == float('inf'):
        print('NO')
    else:
        print(ans)
