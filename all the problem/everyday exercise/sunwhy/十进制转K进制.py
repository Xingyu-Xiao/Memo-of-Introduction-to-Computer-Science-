n, k = map(int, input().split())
s = [i for i in range(10)] + list('ABCDEF')
out = []
while n // k > 0:
    b = n % k
    n //= k
    out.append(s[b])
out.append(s[n])
out.reverse()
print(''.join(map(str, out)))
