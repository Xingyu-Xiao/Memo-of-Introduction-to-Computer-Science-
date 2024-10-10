s = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
a = input()
try:
    a = int(a)
    y = []
    if a >= 1000:
        y.extend(['M'] * int(str(a)[0]))
        a -= (a // 1000) * 1000
    num_CM = a // 900
    y.extend(['CM'] * num_CM)
    a = a - num_CM * 900
    num_D = a // 500
    a -= 500 * num_D
    y.extend(['D'] * num_D)
    num_CD = a//400
    a -= num_CD*400
    y.extend(['CD']*num_CD)
    num_c = a // 100
    a -= num_c * 100
    y.extend(['C'] * num_c)
    num_XC = a // 90
    a -= num_XC * 90
    y.extend(['XC'] * num_XC)
    num_L = a // 50
    a -= num_L * 50
    y.extend(['L'] * num_L)
    num_XL = a // 40
    a -= num_XL * 40
    y.extend(['XL'] * num_XL)
    num_X = a // 10
    a -= num_X * 10
    y.extend(['X'] * num_X)
    num_IX = a // 9
    a -= num_IX * 9
    y.extend(['IX'] * num_IX)
    num_V = a // 5
    a -= num_V * 5
    y.extend(['V'] * num_V)
    num_IV = a // 4
    a -= num_IV * 4
    y.extend(['IV'] * num_IV)
    y.extend(['I'] * a)
    print(''.join(y))
except ValueError:
    k = 0
    for i in range(len(a)):
        if i < len(a)-1:
            if a[i] == 'I':
                if a[i+1] == 'V':
                    k -= 2
                elif a[i+1] == 'X':
                    k -= 2
            elif a[i] == 'X':
                if a[i+1] == 'L':
                    k -= 20
                elif a[i+1] == 'C':
                    k -= 20
            elif a[i] == 'C':
                if a[i+1] == 'D':
                    k -= 200
                elif a[i+1] == 'M':
                    k -= 200
        k += s[a[i]]
    print(k)
