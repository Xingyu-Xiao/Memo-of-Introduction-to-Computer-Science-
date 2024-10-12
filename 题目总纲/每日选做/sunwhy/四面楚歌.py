n, m = map(int, input().split())
s = [list(map(int, input().split())) for _ in range(n)]
out = []
for i in range(n):
    for j in range(m):
        out.append(s[i][j]*int(str(s[0][j])+str(s[i][m-1])+str(s[n-1][j])+str(s[i][0])))
print(max(out))
