x = list(map(int, input().split()))
abc = max(x)
x.remove(abc)
print(abc-x[0], abc-x[1], abc-x[2])
