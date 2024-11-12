n = int(input())
a = list(map(int, input().split()))
p = True
for i in range(n-1):
    if a[i+1] >= a[i]:
        pass
    else:
        p = False
if p:
    print('YES')
else:
    print('NO')
