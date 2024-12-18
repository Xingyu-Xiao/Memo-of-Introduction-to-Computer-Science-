from itertools import product
from copy import deepcopy
s = [list(map(int, input().split())) for _ in range(5)]
out = [[0 for _ in range(6)] for _ in range(5)]
dire = [(0, 1), (1, 0), (0, -1), (-1, 0), (0, 0)]
ite = list(product([1, 0], repeat=6))


def change(i, j):
    for dx, dy in dire:
        x, y = i + dx, j + dy
        if 0 <= x < 5 and 0 <= y < 6:
            ss[x][y] = 1 if ss[x][y] == 0 else 0


def extinguish(i):
    for j in range(6):
        if ss[i-1][j] == 1:
            out[i][j] = 1
            change(i, j)
        else:
            out[i][j] = 0


for x in ite:
    ss = deepcopy(s)
    for k in range(6):
        if x[k] == 1:
            change(0, k)
            out[0][k] = 1
        else:
            out[0][k] = 0
    for i in range(1, 5):
        extinguish(i)
    if not any(y == 1 for y in ss[-1]):
        for o in out:
            print(*o)
        break
