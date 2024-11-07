def solve(s, n, m, b):
    count = 1
    b -= s[0][1]
    if b <= 0:
        return s[0][0]
    for i in range(1, n):
        if s[i][0] == s[i-1][0]:
            if count == m:
                continue
            else:
                b -= s[i][1]
                count += 1
        else:
            b -= s[i][1]
            count = 1
        if b <= 0:
            return s[i][0]
    return 'alive'


n_case = int(input())
for _ in range(n_case):
    n, m, b = map(int, input().split())
    s = [tuple(map(int, input().split())) for _ in range(n)]
    s.sort(key=lambda x: (x[0], -x[1]))
    print(solve(s, n, m, b))
