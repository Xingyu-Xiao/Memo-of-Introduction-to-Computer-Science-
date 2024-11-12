n, m = map(int, input().split())
s = [[0 for _ in range(m+2)]]+[[0]+list(map(int, input().split()))+[0] for _ in range(n)]+[[0 for _ in range(m+2)]]


def number(i, j):
    num = 0
    if s[i][j+1] == 0:
        num += 1
    if s[i][j-1] == 0:
        num += 1
    if s[i+1][j] == 0:
        num += 1
    if s[i-1][j] == 0:
        num += 1
    return num


ans = 0
for i in range(1, n+1):
    for j in range(1, m+1):
        if s[i][j] == 1:
            ans += number(i, j)
print(ans)
