n = int(input())
a = list(map(int, input().split()))
r = [True] * (10**6+1)
p = 2
while p*p <= 10**6:
    if r[p]:
        for i in range(p*p, 10**6+1, p):
            r[i] = False
    p += 1
prime = [y for y in range(2, 10**6) if r[y]]
T_prime = set(p*p for p in prime)
result = ['YES' if x in T_prime else 'NO' for x in a]
print('\n'.join(result))
'''
primes = []
for i in range(2, 10**6):
    if r[i]:
        primes.append(i)
    for p in primes:
        if i * p > 10**6:
            break
        r[i * p] = False
        if i % p == 0:
            break
'''