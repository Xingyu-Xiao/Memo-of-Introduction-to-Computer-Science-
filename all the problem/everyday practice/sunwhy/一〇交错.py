s = list(input())
i = 1
y = []
for index, x in enumerate(s[:len(s)-1]):
    if x != s[index+1]:
        i += 1
    else:
        y.append(i)
        i = 1
y.append(i)
print(max(y))
