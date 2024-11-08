n = int(input())
s = list(map(int, input().split()))
ss = list(zip(s, [i for i in range(1, n+1)]))
ss.sort()
output = [x[1] for x in ss]
print(*output)
out = 0
q = []
for x in ss[:n-1]:
    out = out + x[0]
    q.append(out)
print(f'{(sum(q)/n):.2f}')
