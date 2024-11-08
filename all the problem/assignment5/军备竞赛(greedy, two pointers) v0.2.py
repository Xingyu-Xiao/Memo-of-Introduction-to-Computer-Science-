def f(p, s):
    s.sort()
    i = 0
    j = len(s)-1
    out = 0
    while i <= j:
        if p >= s[i]:
            out += 1
            p -= s[i]
            i += 1
        else:
            if j-i < 2:
                break
            else:
                if out > 0:
                    p += (s[j]-s[i])
                    i += 1
                    j -= 1
                else:
                    break
    return out


P = int(input())
S = list(map(int, input().split()))
print(f(P, S))
