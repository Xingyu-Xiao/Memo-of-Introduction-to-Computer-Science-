n, k = map(int, input().split())
a = list(map(int, input().split()))
sum_a = sum(a)
a.sort()
for i in range(n):
    if a[-1] > sum_a/k:
        k -= 1
        sum_a -= a.pop()
    else:
        print(f'{sum_a/k:.3f}')
        break
