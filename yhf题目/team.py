a = int(input())


def f():
    data = []
    y = 0
    for i in range(a):
        s = input()
        data.append(s)
    return data


b = f()
i = 0
for line in b:
    ss = list(line.split())
    for j in range(len(ss)):
        ss[j] = int(ss[j])
    value = ss[0] + ss[1] + ss[2]
    if int(value) > 1:
        i += 1
print(i)
