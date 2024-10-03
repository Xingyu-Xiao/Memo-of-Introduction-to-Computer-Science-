a = int(input())
s = []
for i in range(1, a+1):
    s.append(int(input()))
for x in s:
    if 360 % (180-x) == 0:
        print('YES')
    else:
        print('NO')
