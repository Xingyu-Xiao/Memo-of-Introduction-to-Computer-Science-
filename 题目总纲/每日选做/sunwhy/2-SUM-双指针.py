n, k = map(int, input().split())
a = list(map(int, input().split()))
out = 0
i = 0
j = len(a)-1
while i < j:
    if a[i] + a[j] == k:
        out += 1
        i += 1
        j -= 1
    elif a[i] + a[j] < k:
        i += 1
    else:
        j -= 1
print(out)
