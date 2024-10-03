s = []
for n in range(1, 1000):
    # if set(str(i)) <= {'4', '7'}:
    # if all(x in '47' for x in str(i)):
    q = True
    i = n
    while i > 0:
        if i % 10 in [4, 7]:
            i //= 10
        else:
            q = False
            break
    if q:
        s.append(n)
a = int(input())
k = True
for x in s:
    if a % x == 0:
        k = False
if k:
    print('NO')
else:
    print('YES')
