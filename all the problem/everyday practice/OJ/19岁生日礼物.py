for _ in range(int(input())):
    a = input()
    if '19' in a or int(a) % 19 == 0:
        print('Yes')
    else:
        print('No')
