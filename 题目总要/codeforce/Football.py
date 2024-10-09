a = list(input())
s = 0
for i in range(len(a)):
    if a[i:i+7] == ['1', '1','1','1','1','1','1'] or a[i:i+7] == ['0', '0','0','0','0','0','0']:
        s = 1
if s == 0:
    print('NO')
else:
    print('YES')
