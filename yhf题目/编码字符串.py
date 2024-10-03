string = input().lower()
output = []
s = 1
for i in range(len(string)-1):
    if string[i] == string[i+1]:
        s += 1
    else:
        output.append((string[i], s))
        s = 1
output.append((string[-1], s))
for x in output:
    print('('+','.join(map(str, x))+')', end='')
