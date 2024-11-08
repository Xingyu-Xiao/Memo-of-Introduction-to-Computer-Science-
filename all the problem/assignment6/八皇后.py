ans = []
a = [None for i in range(9)]


def f(t=1):
    if t == 9:
        ans.append(''.join(map(str, a[1:])))
    else:
        for j in range(1, 9):
            for i in range(1, t):
                if j == a[i] or abs(t-i) == abs(j-a[i]):
                    break
            else:
                a[t] = j
                f(t+1)


f()
for i in range(int(input())):
    print(ans[int(input())-1])
