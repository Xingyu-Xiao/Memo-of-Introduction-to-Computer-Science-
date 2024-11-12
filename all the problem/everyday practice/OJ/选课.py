n = int(input())
k = int(input())
a = list(map(int, input().split()))
for i in range(k):
    pos = 0
    for j in range(1, n):
        if a[-j] > a[-j-1]:
            pos = j+1
            break
    if pos == 0:
        a.reverse()
    else:
        least = a[-pos]
        lea = []
        for j in range(1, pos):
            if a[-j] > least:
                lea.append(a[-j])
        l_pos = a.index(min(lea))
        a[-pos], a[l_pos] = a[l_pos], a[-pos]
        a = a[:n-pos+1] + list(reversed(a[n-pos+1:]))
print(*a)

