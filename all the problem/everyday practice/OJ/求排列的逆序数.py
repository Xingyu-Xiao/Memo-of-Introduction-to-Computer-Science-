import bisect
n = int(input())
a = list(map(int, input().split()))
count = 0
lis = [a[0]]
for i in range(1, n):
    index = bisect.bisect_left(lis, a[i])
    count += (i-index)
    bisect.insort(lis, a[i])
print(count)
