import sys
sys.setrecursionlimit(30000)


def greed(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n == 4:
        return 3
    elif n == 5:
        return 2
    elif n == 2:
        return 1
    if n % 2 == 1:
        if ((n-1)//2) % 2 == 0:
            result = greed(n-2) + 1
        else:
            result = greed((n-1)//2) + 1
    else:
        if (n//2) % 2 == 0:
            result = greed(n-2) + 1
        else:
            result = greed(n//2 - 1) + n//2
    return result


def solve(a):
    results = []
    for x in a:
        results.append(greed(x))
    return results


a = list(map(int, sys.stdin.read().splitlines()))
print('\n'.join(map(str, solve(a[1:]))))
