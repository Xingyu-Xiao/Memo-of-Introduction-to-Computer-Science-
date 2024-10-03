import math
a = int(input())
s = []
for i in range(a):
    s.append(int(input()))
'''
for x in s:
    cell = [0]*x
    for i in range(1, x+1):
        for j in range(1, x+1):
            if j % i == 0:
                if cell[j-1] == 0:
                    cell[j-1] = 1
                else:
                    cell[j-1] = 0
    print(cell.count(1))
'''
for x in s:
    print(math.isqrt(x))
