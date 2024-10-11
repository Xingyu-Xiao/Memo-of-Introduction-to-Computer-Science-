s = [1, 0, 10, 9, 8, 7, 6, 5, 4, 3, 2]
n = int(input())
a = [list(input()) for _ in range(n)]
for x in a:
    if x[17] == 'X':
        x[17] = 10
    x = list(map(int, x))
    k = (7*x[0] + 9*x[1] + 10*x[2] +5*x[3] +8*x[4]+4*x[5] +2*x[6]+x[7]+6*x[8]+3*x[9]+7*x[10]+9*x[11]
         +10*x[12]+5*x[13]+8*x[14]+4*x[15]+2*x[16])
    k = k % 11
    if s[k] == x[17]:
        print('YES')
    else:
        print('NO')
