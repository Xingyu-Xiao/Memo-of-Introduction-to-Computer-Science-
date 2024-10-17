row, col, k = map(int, input().split())
board = {}
n = 0
for _ in range(k):
    r, s, p, t = map(int, input().split())
    up = min(s+p//2, col)
    down = max(s-p//2, 1)
    left = max(r-p//2, 1)
    right = min(r+p//2, row)
    if t == 1:
        n += 1
        for i in range(down, up+1):
            for j in range(left, right+1):
                board[(i, j)] = board.get((i, j), 0) + 1
    else:
        for i in range(down, up+1):
            for j in range(left, right+1):
                board[(i, j)] = -1
out = 0
if n > 0:
    for value in board.values():
        if value == n:
            out += 1
    print(out)
else:
    print(row*col - len(board))
