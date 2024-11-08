n = int(input())
s = list(input().split())
for i in range(n):
    p = False
    for j in range(n-i-1):
        if s[j] + s[j+1] < s[j+1] + s[j]:
            s[j], s[j+1] = s[j+1], s[j]
            p = True
    if not p:
        break
print(''.join(s), ''.join(reversed(s)))
