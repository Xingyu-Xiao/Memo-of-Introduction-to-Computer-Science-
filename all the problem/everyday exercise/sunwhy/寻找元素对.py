n = int(input())
a = list(map(int, input().split()))
k = int(input())
a.sort()
s = 0
for x in a:
    if k - x in a:
        s += 1
print(s//2)
