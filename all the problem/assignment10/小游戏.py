from collections import deque
dire = [(1, 0), (-1, 0), (0, 1), (0, -1)]


def bfs(x, y, board, goal):
    visited = {}
    min_x = float('inf')
    queue = deque([(x, y, -1, 0)])
    while queue:
        x, y, d, num = queue.popleft()
        for i, (dx, dy) in enumerate(dire):
            nx, ny = x + dx, y + dy
            new_num = num if i == d else num + 1
            if [ny, nx] == goal:
                min_x = min(min_x, new_num)
                continue
            if (0 <= nx < len(board) and 0 <= ny < len(board[0]) and
                    board[nx][ny] != 'X' and new_num < visited.get((nx, ny, i), float('inf'))):
                visited[(nx, ny, i)] = new_num
                queue.append((nx, ny, i, new_num))
    return min_x


n = 0
while True:
    n += 1
    w, h = map(int, input().split())
    if w == h == 0:
        break
    bo = [' '*(w+2)]+[' '+input()+' ' for _ in range(h)]+[' '*(w+2)]
    print(f'Board #{n}:')
    m = 0
    while True:
        m += 1
        card = list(map(int, input().split()))
        if card == [0, 0, 0, 0]:
            break
        ca1 = card[0:2]
        ca2 = card[2:]
        k = bfs(ca1[1], ca1[0], bo, ca2)
        if k != float('inf'):
            print(f'Pair {m}: {k} segments.')
        else:
            print(f'Pair {m}: impossible.')
    print()
