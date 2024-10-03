def matrix():
    s = []
    for j in range(5):
        s.append(input())
    return s


a = matrix()
for x in a:
    e = abs(a.index(x) - 2)
    p = list(x.split())
    if "1" in p:
        q = p.index("1")
        y = abs(q-2)
        print(e+y)
