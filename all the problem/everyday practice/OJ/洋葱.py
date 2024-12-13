n = int(input())
matrix = [list(map(int,input().split())) for _ in range(n)]
ans = []
i, j = 0, n-1
while i < j:
    ans.append(sum(matrix[i][k] for k in range(i, j+1))+sum(matrix[j][k] for k in range(i, j+1))+sum(matrix[k][i] for k in range(i+1, j))+sum(matrix[k][j] for k in range(i+1, j)))
    i += 1
    j -= 1
if n % 2 == 1:
    ans.append(matrix[n//2][n//2])
print(max(ans))
