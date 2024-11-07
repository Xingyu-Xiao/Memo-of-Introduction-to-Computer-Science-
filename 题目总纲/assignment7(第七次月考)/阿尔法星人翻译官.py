word = {'zero':0, 'one':1, 'two':2, 'three':3, 'four':4, 'five':5, 'six':6,
        'seven':7, 'eight':8, 'nine':9, 'ten':10, 'eleven':11, 'twelve':12, 'thirteen':13,
        'fourteen':14, 'fifteen':15, 'sixteen':16, 'seventeen':17, 'eighteen':18, 'nineteen':19,
        'twenty':20, 'thirty':30, 'forty':40, 'fifty':50, 'sixty':60, 'seventy':70,
        'eighty':80, 'ninety':90}


def f(a):
    return sum(word[x] for x in a)


def hundred(a):
    if 'hundred' in a:
        index_h = a.index('hundred')
        return sum(word[x] for x in a[:index_h])*100 + f(a[index_h+1:])
    else:
        return f(a)


def thousand(a):
    if 'thousand' in a:
        index_t = a.index('thousand')
        return hundred(a[:index_t])*1000 + hundred(a[index_t+1:])
    else:
        return hundred(a)


def million(a):
    if 'million' in a:
        index_m = a.index('million')
        return thousand(a[:index_m])*1000000 + thousand(a[index_m+1:])
    else:
        return thousand(a)


ans = []
s = list(input().split())
if s[0] == 'negative':
    ans.append('-')
    s = s[1:]
ans.append(str(million(s)))
print(''.join(ans))
