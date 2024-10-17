t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    s = sorted(range(n), key=lambda x: a[x], reverse=True)
    sum_b = 0
    for i in s:
        if sum_b + b[i] < a[i]:
            sum_b += b[i]
            a[i] = 0
        else:
            break
    print(max(sum_b, *a))
    