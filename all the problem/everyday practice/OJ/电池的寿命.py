def solve(s):
    if len(s) == 2:
        return s[0]
    if len(s) == 1:
        return 0
    time = sum(s)/2
    if s[-1] > time:
        a = s.pop()
        b = s.pop()
        s.append(a-b)
        return solve(s) + b
    else:
        return time


while True:
    try:
        n = int(input())
        *s, = map(int, input().split())
        s.sort()
        print(f'{solve(s):.1f}')
    except EOFError:
        break
