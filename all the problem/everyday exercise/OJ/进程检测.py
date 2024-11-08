k = int(input())
for _ in range(k):
    n = int(input())
    s = [list(map(int, input().split())) for _ in range(n)]
    s.sort(key=lambda x: x[1])
    j = 1
    last = s[0][1]
    for i in range(1, n):
        if s[i][0] > last:
            j += 1
            last = s[i][1]
    print(j)
