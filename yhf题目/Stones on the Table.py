a = int(input())
b = list(input())
s = []
for i in range(a-1):
    if b[i] != b[i+1]:
        s.append(i)
print(a-1-len(s))
