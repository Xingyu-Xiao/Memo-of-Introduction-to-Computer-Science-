s = []
while True:
    try:
        a = input()
        if not a:
            break
        else:
            s.append(a)
    except EOFError:
        break
for x in s:
    if x.count('@') != 1:
        print('NO')
    else:
        if x[0] == '@' or x[-1] == '@' or x[0] == '.' or x[-1] == '.':
            print('NO')
        else:
            x = x[x.index('@')-1:]
            if '.' in x:
                if x.index('.') > 2:
                    print('YES')
                else:
                    print('NO')
            else:
                print('NO')
