while True:
    n = int(input())
    if n == 0:
        break
    else:
        s = [(tuple(map(int, input().split()))) for _ in range(n)]
        s.sort()
        j = 1
        max_cost = s[0][1]
        for x in s:
            if x[1] < max_cost:
                j += 1
                max_cost = x[1]
        print(j)
