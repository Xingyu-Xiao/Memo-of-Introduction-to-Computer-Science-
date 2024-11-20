from collections import deque
n, m = map(int, input().split())
s = [list(map(int, input().split())) for _ in range(n)]
if s[0][0] == 1:
    print(0)
else:
    queue = deque([(0, 0)])
    visited = set()
    visited.add((0, 0))
    next_point = ((1, 0), (0, -1), (0, 1), (-1, 0))
    ans = 0
    p = True
    while True:
        new_queue = deque()
        while queue:
            x, y = queue.popleft()
            for dx, dy in next_point:
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < m:
                    if s[nx][ny] == 0:
                        if (nx, ny) not in visited:
                            new_queue.append((nx, ny))
                            visited.add((nx, ny))
                    elif s[nx][ny] == 1:
                        p = False
                        break
            if not p:
                break
        queue = new_queue
        ans += 1
        if not p:
            print(ans)
            break
        if not queue:
            print('NO')
            break
