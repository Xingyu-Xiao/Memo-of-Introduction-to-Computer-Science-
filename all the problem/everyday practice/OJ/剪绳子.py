import heapq
n = int(input())
*s, = map(int, input().split())
heapq.heapify(s)
ans = 0
while len(s) > 1:
    a = heapq.heappop(s)
    b = heapq.heappop(s)
    ans += (a+b)
    heapq.heappush(s, a+b)
print(ans)
