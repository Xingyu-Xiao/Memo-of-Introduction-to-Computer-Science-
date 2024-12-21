from collections import deque
n, k = map(int, input().split())
*s, = map(int, input().split())
a = deque(s[:k])
max0 = max(s[:k])
ans = [max0]
for j in range(k, n):
    a.append(s[j])
    x = a.popleft()
    if x < ans[-1]:
        if ans[-1] > s[j]:
            ans.append(ans[-1])
        else:
            ans.append(s[j])
    else:
        ans.append(max(a))
print(*ans)
