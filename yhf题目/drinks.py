a = int(input())
p = list(input().split())
x = 0
for i in range(a):
    p[i] = int(p[i])
    x = x + p[i]
print(x/a)
