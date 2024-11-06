n = int(input())
while n > 1:
    if n % 2 == 0:
        n = n//2
        print(f'{2*n}/2={n}')
    else:
        print(f'{n}*3+1={n*3+1}')
        n = n*3+1
print('End')
