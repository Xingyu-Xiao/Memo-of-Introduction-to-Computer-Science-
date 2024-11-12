def can_reach(n, c, mid, x):
    c -= 1
    last = x[0]
    for i in range(1, n):
        if x[i] - last >= mid:
            c -= 1
            last = x[i]
        if c == 0:
            return True
    return False


n, c = map(int, input().split())
x = [int(input()) for _ in range(n)]
x.sort()
low, high = 0, (x[-1]-x[0])//(c-1)
while low <= high:
    mid = (low + high) // 2
    if can_reach(n, c, mid, x):
        low = mid + 1
    else:
        high = mid - 1
print(high)
