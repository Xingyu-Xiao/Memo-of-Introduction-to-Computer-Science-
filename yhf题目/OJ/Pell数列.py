n = int(input())
s = [int(input()) for _ in range(n)]
a = [0]*(10**6)
a[0] = 1
a[1] = 2
for i in range(2, 10**6):
    a[i] = (2*a[i-1] + a[i-2]) % 32767
for x in s:
    print(a[x-1])
