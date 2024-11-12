row, line = map(int, input().split())
matrix = ([[0 for _ in range(line+2)]]+[[0]+list(map(int, input().split()))+[0] for _ in range(row)]
          + [[0 for _ in range(line+2)]])
updated_matrix = [[0 for _ in range(line)] for _ in range(row)]
for i in range(1, row+1):
    for j in range(1, line+1):
        alive = [matrix[i][j-1], matrix[i-1][j], matrix[i][j+1], matrix[i+1][j], matrix[i-1][j-1]
                 , matrix[i-1][j+1], matrix[i+1][j+1], matrix[i+1][j-1]].count(1)
        if alive <= 1:
            updated_matrix[i-1][j-1] = 0
        elif alive == 3:
            updated_matrix[i-1][j-1] = 1
        elif alive >= 4:
            updated_matrix[i-1][j-1] = 0
        elif alive == 2:
            updated_matrix[i-1][j-1] = matrix[i][j]
for row in updated_matrix:
    print(*row)
