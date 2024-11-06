n = int(input())
s = list(input())
ss = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
      'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
SS = [x.upper() for x in ss]
for index, x in enumerate(s):
    if x in ss:
        k = ss.index(x)
        kk = (k-n) % 26
        s[index] = ss[kk]
    else:
        i = SS.index(x)
        s[index] = SS[(i-n) % 26]
print(''.join(map(str, s)))
