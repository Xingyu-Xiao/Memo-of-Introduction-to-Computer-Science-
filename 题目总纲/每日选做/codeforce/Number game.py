import bisect


def max_k(arr, k):
    for i in range(1, k+1):
        index = bisect.bisect_right(arr, k-i+1)
        if index == 0:
            return False
        arr = arr[1:index-1]
    return True


t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    j = 0
    while True:
        if max_k(a, j):
            j += 1
        else:
            break
    print(j-1)
