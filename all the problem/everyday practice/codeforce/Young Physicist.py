n = int(input())
s = []
s_1 = []
s_2 = []
s_3 = []
for i in range(n):
    s.append(list(map(int, input().split())))
for x in s:
    s_1.append(x[0])
    s_2.append(x[1])
    s_3.append(x[2])
if sum(s_1) == sum(s_2) == sum(s_3) == 0:
    print('YES')
else:
    print('NO')
