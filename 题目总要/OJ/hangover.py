s = []
while True:
    a = float(input())
    s.append(a)
    if a == 0.00:
        break
for x in s:
    if x > 0:
        p = 0
        i = 1
        while p <= x:
            p += 1/(i+1)
            i += 1
        print(i-1, 'card(s)')
