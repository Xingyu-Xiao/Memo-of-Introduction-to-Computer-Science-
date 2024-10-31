total, n = map(int, input().split())
qq = [True]*(total+1)
for i in range(n):
    q = list(map(int, input().split()))
    for j in range(q[0], q[1]+1):
        qq[j] = False
print(sum(qq))
