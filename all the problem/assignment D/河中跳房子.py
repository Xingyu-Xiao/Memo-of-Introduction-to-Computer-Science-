l, n, m = map(int, input().split())
rock = [0] + [int(input()) for _ in range(n)] + [l]


def check(min_dis):
    num = 0
    j = 0
    for i in range(1, n+2):
        if rock[i] - rock[j] < min_dis:
            num += 1
        else:
            j = i
    if num <= m:
        return True
    else:
        return False


left, right = 0, l+1
while left < right:
    mid = (left + right) // 2
    if check(mid):
        left = mid + 1
    else:
        right = mid
print(right-1)
