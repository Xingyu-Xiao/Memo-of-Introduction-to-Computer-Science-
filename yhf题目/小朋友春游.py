n = int(input())
a = list(map(int, input().split()))
a.sort()
for i in range(n, 0, -1):
    if i in a:
        index = a.index(i)
        break
other = a[index+1:]
our = a[:index+1]
original = [i for i in range(1, n+1)]
astray = [x for x in original if x not in our]
print(' '.join(map(str, astray)))
print(' '.join(map(str, other)))
