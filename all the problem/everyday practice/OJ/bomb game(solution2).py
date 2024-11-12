row, col, k = map(int, input().split())
possible_positions = set((i, j) for i in range(1, row + 1) for j in range(1, col + 1))

for _ in range(k):
    r, s, p, t = map(int, input().split())
    radius = p // 2

    bomb_range = set()
    for i in range(max(1, r - radius), min(row, r + radius) + 1):
        for j in range(max(1, s - radius), min(col, s + radius) + 1):
            bomb_range.add((i, j))

    if t == 1:
        possible_positions.intersection_update(bomb_range)
    else:
        possible_positions.difference_update(bomb_range)

out = len(possible_positions)
print(out)
