n = int(input())
s = []
for i in range(1, n+1):
    if i % 7 == 0 or str(i)[0] == '7' or str(i)[-1] == '7':
        pass
    else:
        s.append(i)
ss = map(lambda x: x**2, s)
print(sum(ss))
