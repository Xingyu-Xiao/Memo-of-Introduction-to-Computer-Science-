n = int(input())
a = [input() for _ in range(n)]
u = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
for x in a:
    if x[0] == 'R' and 'C' in x and x[1] in u:
        index_c = x.index('C')
        row = (x[1:index_c])
        col = int(x[index_c+1:])
        out = []
        while col > 0:
            col -= 1
            n = col % 26
            col = col // 26
            out.append(chr(n+65))
        out.reverse()
        print(''.join(out)+row)
    else:
        out = 0
        for y in x:
            try:
                row = int(y)
                index = x.index(y)
                break
            except ValueError:
                out = 26*out + (ord(y)-64)
        print(f'R{x[index:]}C{out}')
