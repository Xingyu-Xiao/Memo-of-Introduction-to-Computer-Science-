n = int(input())
print('*')
for i in range(1, n-1):
    s = [' ']*(i-1)
    print('*'+''.join(s)+'*')
print('*'*n)
