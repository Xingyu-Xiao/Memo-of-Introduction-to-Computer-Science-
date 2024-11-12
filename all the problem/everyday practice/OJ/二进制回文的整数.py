b = int(input())
a = bin(b)[2:]
a = ''.join(reversed(a))
a = int(a, 2)
if a == b:
    print('Yes')
else:
    print('No')
