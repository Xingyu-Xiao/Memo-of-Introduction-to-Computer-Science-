n = int(input())
s = [int(input()) for _ in range(n)]
m = [0]*20
m[0] = 1
m[1] = 1
for i in range(2, 20):
    m[i] = m[i-1] + m[i-2]
for x in s:
    print(m[x-1])
