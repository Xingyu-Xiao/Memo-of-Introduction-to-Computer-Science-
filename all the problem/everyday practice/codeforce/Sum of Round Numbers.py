a = int(input())


def f():
    s = []
    for j in range(a):
        s.append(input())
    return s


b = f()
for i in range(a):
    p = int(b[i])
    if p % 10000 == 0:
        print(1)
        print(10000)
    else:
        x = p % 10
        y = p % 100
        z = p % 1000
        if p//1000 != 0:
            if z == 0:
                print(1)
                print(p)
            else:
                if y == 0:
                    print(2)
                    print(p-z, z-y)
                else:
                    if x == 0:
                        if z-y != 0:
                            print(3)
                            print(p-z, z-y, y-x)
                        else:
                            print(2)
                            print(p-z, y-x)
                    else:
                        if z-y != 0:
                            if y-x != 0:
                                print(4)
                                print(p-z, z-y, y-x, x)
                            else:
                                print(3)
                                print(p-z, z-y, x)
                        else:
                            if y-x != 0:
                                print(3)
                                print(p-z, y-x, x)
                            else:
                                print(2)
                                print(p-z, x)
        else:
            if p//100 != 0:
                if y == 0:
                    print(1)
                    print(z-y)
                else:
                    if x == 0:
                        print(2)
                        print(z-y, y-x)
                    else:
                        if y-x != 0:
                            print(3)
                            print(z-y, y-x, x)
                        else:
                            print(2)
                            print(z-y, x)
            else:
                if p//10 != 0:
                    if x == 0:
                        print(1)
                        print(p)
                    else:
                        print(2)
                        print(p-x, x)
                else:
                    print(1)
                    print(x)
