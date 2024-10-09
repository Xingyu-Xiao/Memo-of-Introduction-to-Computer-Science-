'''
a = list(input())
if 'h' in a:
    index_h = a.index('h')
    a = a[index_h+1:]
    if 'e' in a:
        index_e = a.index('e')
        a = a[index_e+1:]
        if 'l' in a:
            index_l = a.index('l')
            a = a[index_l+1:]
            if 'l' in a:
                index_l = a.index('l')
                a = a[index_l+1:]
                if 'o' in a:
                    print('YES')
                else:
                    print('NO')
            else:
                print('NO')
        else:
            print('NO')
    else:
        print('NO')
else:
    print('NO')
'''


a = input()
target = 'hello'
j = 0
for x in a:
    if x == target[j]:
        j += 1
        if j == len(target):
            print('YES')
            break
if j < len(target):
    print('NO')
