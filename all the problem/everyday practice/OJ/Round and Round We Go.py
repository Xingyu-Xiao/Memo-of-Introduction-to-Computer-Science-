while True:
    try:
        p = True
        s = input()
        n = len(s)
        int_s = int(s)
        s_2 = s + s
        lis = [str(int_s*i).zfill(n) for i in range(2, n+1)]
        for x in lis:
            if x in s_2:
                continue
            else:
                p = False
                break
        if p:
            print(f'{s} is cyclic')
        else:
            print(f'{s} is not cyclic')
    except EOFError:
        break
