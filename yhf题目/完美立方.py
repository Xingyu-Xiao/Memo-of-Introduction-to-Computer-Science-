n = int(input())
s = []
a = [i**3 for i in range(n+1)]
ss = {a[i]: i for i in range(n+1)}
for i in range(2, n):
    for j in range(i, n):
        for k in range(j, n):
            b = a[i] + a[j] + a[k]
            if b in ss:
                s.append((ss[b], (i, j, k)))
s.sort()
print('\n'.join(map(lambda x: f'Cube = {x[0]}, Triple = ({x[1][0]},{x[1][1]},{x[1][2]})', s)))
