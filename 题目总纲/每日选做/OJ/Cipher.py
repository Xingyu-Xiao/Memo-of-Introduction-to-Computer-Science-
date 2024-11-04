def move(t, st, key):
    for _ in range(t):
        st = key[st]
    return st


def cir(num, key):
    ret = []
    for i in range(num):
        x = key[i]
        count = 1
        while x != i:
            count += 1
            x = key[x]
        ret.append(count)
    return ret


while True:
    n = int(input())
    if n == 0:
        break
    a = list(map(lambda x: int(x)-1, input().split()))
    c = cir(n, a)
    while True:
        s = input().split(' ', 1)
        k = int(s[0])
        if k == 0:
            break
        words = f'{s[1]:<{n}}'
        ans = ['']*n
        for i in range(n):
            ans[move(k % c[i], i, a)] = words[i]
        print(''.join(ans))
    print()
