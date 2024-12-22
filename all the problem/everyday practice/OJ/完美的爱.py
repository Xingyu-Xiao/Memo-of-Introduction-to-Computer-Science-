n = int(input())
gifts = list(map(lambda x: int(x)-520, input().split()))
prefix_sum = 0
ps = {0: -1}
length = 0
for i in range(n):
    prefix_sum += gifts[i]
    if prefix_sum in ps:
        length = max(i - ps[prefix_sum], length)
    else:
        ps[prefix_sum] = i
print(length*520)
