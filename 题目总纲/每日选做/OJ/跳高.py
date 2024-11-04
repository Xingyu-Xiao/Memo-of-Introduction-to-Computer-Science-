from bisect import bisect_left
n = int(input())
a = list(map(int, input().split()))
a.reverse()
lis = []
for x in a:
    index = bisect_left(lis, x)
    if index != len(lis):
        lis[index] = x
    else:
        lis.append(x)
print(len(lis))
