from sys import stdin
a = input()
q = [0]*(len(a))
for i in range(1, len(a)):
    if a[i] == a[i-1]:
        q[i] = q[i-1] + 1
    else:
        q[i] = q[i-1]
n = int(input())
s = []
for i in range(n):
    x, y = map(int, stdin.readline().strip().split())
    s.append([x, y])
o = []
for ss in s:
    x = ss[0]
    y = ss[1]
    o.append(q[y-1]-q[x-1])
print('\n'.join(map(str, o)))
