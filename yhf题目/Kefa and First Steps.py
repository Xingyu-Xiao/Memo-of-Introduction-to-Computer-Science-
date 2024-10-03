a = int(input())
b = list(map(int, input().split()))
s = [b[0]]
ss = []
for i in range(1, a):
    if b[i-1] <= b[i]:
        s.append(b[i])
    else:
        ss.append(s)
        s = [b[i]]
ss.append(s)
length = map(len, ss)
print(max(length))
