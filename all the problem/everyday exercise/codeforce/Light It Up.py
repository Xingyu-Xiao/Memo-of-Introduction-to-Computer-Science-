n, M = map(int, input().split())
a = list(map(int, input().split()))
time_gap = [0]*(n+1)
time_gap[0] = a[0]
for i in range(1, n):
    time_gap[i] = a[i] - a[i-1]
time_gap[-1] = M - a[-1]
time = [0]*(n+1)
time[0] = time_gap[0]
for i in range(2, n+1, 2):
    time[i] = time[i-2] + time_gap[i]
total = time[-1] if n % 2 == 0 else time[-2]
out = total
if n > 1:
    for j in range(0, n, 2):
        new_time = 0
        if j != 0 and j != n - 1:
            if a[j] + 1 != a[j+1] or a[j] - 1 != a[j-1]:
                new_time = 2*time[j] + M - a[j] - 1 - total
        elif j == 0:
            if a[j] + 1 != a[j+1] or a[j] - 1 != 0:
                new_time = 2*time[j] + M - a[j] - 1 - total
        elif j == n-1:
            if a[j] + 1 != M or a[j] - 1 != a[j-1]:
                new_time = 2 * time[j] + M - a[j] - 1 - total
        out = max(out, new_time)
else:
    out = max(out, a[0] + M - 1 - total)
print(out)
