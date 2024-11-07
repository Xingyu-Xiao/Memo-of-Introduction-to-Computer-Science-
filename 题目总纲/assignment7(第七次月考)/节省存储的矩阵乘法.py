n, m_1, m_2 = map(int, input().split())
s_1 = [[0 for _ in range(n)] for _ in range(n)]
s_2 = [[0 for _ in range(n)] for _ in range(n)]
for _ in range(m_1):
    i, j, k = map(int, input().split())
    s_1[i][j] = k
for _ in range(m_2):
    i, j, k = map(int, input().split())
    s_2[i][j] = k
ans = [[0 for _ in range(n)] for _ in range(n)]
for i in range(n):
    for j in range(n):
        ans[i][j] = sum(s_1[i][k]*s_2[k][j] for k in range(n))
        if ans[i][j] != 0:
            print(i, j, ans[i][j])
