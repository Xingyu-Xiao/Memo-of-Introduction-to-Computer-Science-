def solve(k, n):
    matrix = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(i, n):
            if k > 0:
                if i == j:
                    matrix[i][j] = 1
                    k -= 1
                else:
                    if k == 1:
                        continue
                    else:
                        matrix[i][j] = 1
                        matrix[j][i] = 1
                        k -= 2
            else:
                return matrix
    return matrix


n, k = map(int, input().split())
if k > n**2:
    print(-1)
else:
    out = solve(k, n)
    for x in out:
        print(*x)
