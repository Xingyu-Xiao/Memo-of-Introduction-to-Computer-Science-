a = int(input())
s = []
x = 0
for i in range(a):
    s.append(input())
for y in s:
    if '++' in y:
        x += 1
    elif '--' in y:
        x -= 1
print(x)
