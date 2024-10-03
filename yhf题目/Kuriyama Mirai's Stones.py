n = int(input())
v = list(map(int, input().split()))
sum_v = [0]*n
for i in range(n):
    sum_v[i] = v[i] + sum_v[i-1]
vv = sorted(v)
sum_vv = [0]*n
for i in range(n):
    sum_vv[i] = vv[i] + sum_vv[i-1]
m = int(input())
s = [list(map(int, input().split())) for _ in range(m)]
output = []
for ss in s:
    t = ss[0]
    l = ss[1]
    r = ss[2]
    if t == 1:
        if l == 1:
            output.append(sum_v[r-1])
        else:
            output.append(sum_v[r-1]-sum_v[l-2])
    elif t == 2:
        if l == 1:
            output.append(sum_vv[r-1])
        else:
            output.append(sum_vv[r-1]-sum_vv[l-2])
print('\n'.join(map(str, output)))
