a = int(input())
s = 'I hate '
for i in range(1, a):
    if i % 2 != 0:
        s = s + 'that I love '
    else:
        s = s + 'that I hate '
print(f'{s}it')
