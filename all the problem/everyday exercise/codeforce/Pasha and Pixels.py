n, m, k = map(int, input().split())
s = [list(map(int, input().split())) for _ in range(k)]
l = [[0 for _ in range(m+2)] for _ in range(n+2)]
for index, ss in enumerate(s):
    i = ss[0]
    j = ss[1]
    l[i][j] = 1
    if (l[i+1][j+1] == l[i][j+1] == l[i+1][j] == 1 or l[i][j-1] == l[i-1][j-1] == l[i-1][j] == 1 or
            l[i+1][j] == l[i][j-1] == l[i+1][j-1] == 1 or l[i-1][j+1] == l[i-1][j] == l[i][j+1] == 1):
        print(index+1)
        break
else:
    print(0)
