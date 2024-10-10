s = []
while True:
    a, b, c, d = map(int, input().split())
    if a == b == c == d == -1:
        break
    else:
        s.append((a, b, c, d))
for index, x in enumerate(s):
    a, b, c, d = x
    if a == b == c:
        print(f'Case {index+1}: the next triple peak occurs in {21252-d+a} days.')
    else:
        while True:
            k = min([a, b, c])
            if a == b == c:
                print(f'Case {index+1}: the next triple peak occurs in {a-d} days.')
                break
            elif c == k:
                c += 33
            elif b == k:
                b += 28
            elif a == k:
                a += 23
