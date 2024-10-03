a = input()
b = input()
m = max(len(a), len(b))
if len(a) < m:
    a = '0'*(m-len(a)) + a
else:
    b = '0'*(m-len(b)) + b
s = [int(a[i]) + int(b[i]) for i in range(m)]
s.reverse()
for index, x in enumerate(s):
    if x >= 10 and index < len(s)-1:
        s[index] -= 10
        s[index+1] += 1
if set(s) != {0}:
    print(''.join(map(str, reversed(s))).lstrip('0'))
else:
    print(0)
