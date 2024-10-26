n = int(input())
s = [tuple(map(int, input().split())) for _ in range(n)]
a = [x[1]-x[0]+1 for x in s]
c = [0]*22
c[2] = 1
c[3] = 2
for i in range(4,22):
    c[i] = c[i-1] + c[i-2]
for y in a:
    print(c[y])
