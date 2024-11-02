import math
index = 1
k = 1
k_index = [0, 1]
while index <= 2147483647:
    k += 1
    w = len(str(k))
    if w == 1:
        index += k
    elif w == 2:
        index += 2*(k-9) + 9
    elif w == 3:
        index += 189 + 3*(k-99)
    elif w == 4:
        index += 2889 + 4*(k-999)
    else:
        index += 38889 + 5*(k-9999)
    k_index.append(index)


def f(x):
    for i in range(1, 2147483647):
        if k_index[i-1] < x <= k_index[i]:
            return i


def number(x):
    n = x - k_index[f(x)-1]
    if n < 10:
        return str(n)
    elif n < 190:
        p = (n-9) % 2
        q = math.ceil((n-9)/2) + 9
        return str(q)[p-1]
    elif n < 2890:
        p = (n-189) % 3
        q = math.ceil((n-189) / 3) + 99
        return str(q)[p-1]
    elif n < 38890:
        p = (n-2889) % 4
        q = math.ceil((n-2889) / 4) + 999
        return str(q)[p-1]
    else:
        p = (n-38889) % 5
        q = math.ceil((n-38889) / 5) + 9999
        return str(q)[p-1]


t = int(input())
out = [number(int(input())) for _ in range(t)]
print('\n'.join(out))
