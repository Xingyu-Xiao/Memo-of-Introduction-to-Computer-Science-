line1 = list('qwertyuiop')
line2 = list('asdfghjkl;')
line3 = list('zxcvbnm,./')
h = input()
a = list(input())
out = []
for x in a:
    if h == 'R':
        if x in line1:
            index = line1.index(x)
            out.append(line1[index-1])
        elif x in line2:
            index = line2.index(x)
            out.append(line2[index-1])
        elif x in line3:
            index = line3.index(x)
            out.append(line3[index-1])
    elif h == 'L':
        if x in line1:
            index = line1.index(x)
            out.append(line1[index+1])
        elif x in line2:
            index = line2.index(x)
            out.append(line2[index+1])
        elif x in line3:
            index = line3.index(x)
            out.append(line3[index+1])
print(''.join(out))
