d = int(input())
n = int(input())
s = {}
for _ in range(n):
    x, y, i = map(int, input().split())
    up = min(y+d, 1024)
    down = max(y-d, 0)
    left = max(x-d, 0)
    right = min(x+d, 1024)
    for k in range(left, right+1):
        for l in range(down, up+1):
            s[(k, l)] = s.get((k, l), 0) + i
out_max = 0
out_num = 1
for location in s.values():
    if out_max == location:
        out_num += 1
    elif out_max < location:
        out_max = location
        out_num = 1
print(out_num, out_max)
