n = int(input())
nums = []
while len(nums) < n * n:
    nums.extend(input().split())
matrix = [list(map(int, nums[i * n:(i + 1) * n])) for i in range(n)]
prefix_sum = [[0 for _ in range(n+1)] for _ in range(n)]
for i in range(n):
    for j in range(n):
        if j == 0:
            prefix_sum[i][j+1] = matrix[i][j]
        else:
            prefix_sum[i][j+1] = prefix_sum[i][j] + matrix[i][j]
temp = []
for j in range(1, n+1):
    for k in range(j, n+1):
        p_sum = [prefix_sum[i][k] - prefix_sum[i][j-1] for i in range(n)]
        dp_jk = [0]*n
        for i in range(n):
            dp_jk[i] = max(dp_jk[i-1]+p_sum[i], p_sum[i])
        temp.append(max(dp_jk))
print(max(temp))
