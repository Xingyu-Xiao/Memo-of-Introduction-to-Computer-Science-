out = []


def f(matrix):
    if matrix:
        m = len(matrix)
        n = len(matrix[0])
        for i in range(n):
            out.append(matrix[0][i])
        if m > 1:
            for j in range(1, m):
                out.append(matrix[j][n - 1])
            if n == 1:
                return
            for k in range(n-2, -1, -1):
                out.append(matrix[m-1][k])
        if m == 1 or m == 2:
            return
        for b in range(m-2, 0, -1):
            out.append(matrix[b][0])
        if n == 2:
            return
        new_matrix = [[matrix[i][j] for j in range(1, n-1)] for i in range(1, m-1)]
        f(new_matrix)
    else:
        return

