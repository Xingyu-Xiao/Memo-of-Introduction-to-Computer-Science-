a, b = map(int, input().split())
s = []
p = True
for i in range(a, b+1):
    i_1, i_2, i_3 = map(int,[str(i)[0], str(i)[1], str(i)[2]])
    if i_1**3 + i_2**3 + i_3**3 == i:
        s.append(i)
        p = False
if not p:
    print(' '.join(map(str, s)))
else:
    print('NO')
