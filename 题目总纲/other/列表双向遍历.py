s = list(map(int, input().split()))
s.sort()
i = 0
j = len(s)-1
out = []
while True:
    p = False
    out_1 = []
    while True:
        out_1.append(s[i])
        i += 1
        if s[i-1] % 2 == 0 and len(out_1) > 1:
            out.extend(out_1)
            break
        if i == j:
            out.extend(out_1)
            out.append(s[i])
            p = True
            break
    if p:
        break
    out_2 = []
    while True:
        out_2.append(s[j])
        j -= 1
        if s[j+1] % 3 == 0 and len(out_2) > 1:
            out.extend(out_2)
            break
        if i == j:
            out.extend(out_2)
            out.append(s[j])
            p = True
            break
    if p:
        break
print(' '.join(map(str, out)))
