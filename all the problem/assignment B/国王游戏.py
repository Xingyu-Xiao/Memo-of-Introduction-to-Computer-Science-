n = int(input())
a, b = map(int, input().split())
s = [tuple(map(int, input().split())) for _ in range(n)]
s.sort(key=lambda x: x[0]*x[1])
ans = [0]*n
ans[0] = a
for i in range(1, n):
    ans[i] = ans[i-1]*s[i-1][0]
print(max(ans[i]//s[i][1] for i in range(n)))
