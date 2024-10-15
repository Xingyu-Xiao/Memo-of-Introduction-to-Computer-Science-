h = int(input())
n = int(input())
h = 2*h - n/2
sc = [list(map(float, input().split())) for _ in range(n)]
sc.sort(key=lambda x: x[0]*x[1], reverse=True)
out = 0
for s, c in sc:
    if 5/s <= h:
        h -= 5/s
        out += 5*c
    else:
        out += h*s*c
        break
print(f'{out:.1f}')
