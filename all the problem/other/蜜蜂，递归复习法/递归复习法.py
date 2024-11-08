n = int(input())
s = [int(input()) for _ in range(n)]
a = [0]*26
a[1] = 1
a[2] = 2
for i in range(3, 26):
    a[i] = a[i-1] + a[i-2] + i
b = [a[y] for y in s]
print('\n'.join(map(str, b)))
