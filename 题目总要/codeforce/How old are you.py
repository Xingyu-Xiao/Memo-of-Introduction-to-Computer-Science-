a = int(input())
while a > 1:
    if a % 2 == 0:
        a //= 2
        print(f'{2*a}/2={a}')
    else:
        print(f'{a}*3+1={a*3+1}')
        a = a*3 + 1
