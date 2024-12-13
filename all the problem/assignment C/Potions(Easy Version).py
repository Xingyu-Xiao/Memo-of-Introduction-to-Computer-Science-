import heapq
min_heap = []
n = int(input())
s = list(map(int, input().split()))
health = 0
ans = 0
for x in s:
    health += x
    if x >= 0:
        ans += 1
    else:
        heapq.heappush(min_heap, x)
        if health < 0:
            health -= heapq.heappop(min_heap)
        else:
            ans += 1
print(ans)
