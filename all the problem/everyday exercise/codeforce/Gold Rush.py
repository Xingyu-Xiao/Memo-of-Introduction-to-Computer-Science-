from functools import lru_cache


@lru_cache(maxsize=None)
def solve(n, m):
    if n == m:
        return True
    if n < m or n % 3 != 0:
        return False
    if solve(n//3, m) or solve((n//3)*2, m):
        return True
    return False


t = int(input())
s = [tuple(map(int, input().split())) for _ in range(t)]
for x, y in s:
    if solve(x, y):
        print('YES')
    else:
        print('NO')
