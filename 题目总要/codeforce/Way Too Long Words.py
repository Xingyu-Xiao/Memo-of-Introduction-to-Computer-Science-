n = int(input())
s = []
for i in range(n):
    s.append(input())
for x in s:
    if len(x) <= 10:
        print(x)
    else:
        print(f'{x[0]}{len(x)-2}{x[-1]}')
