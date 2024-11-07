import bisect
n = int(input())
s = list(map(int, input().split()))
lis = []
for x in s:
    index = bisect.bisect_left(lis, x)
    if index == len(lis):
        lis.append(x)
    else:
        lis[index] = x
print(len(lis))
