a = input()
b = input()
a = a.lower()
b = b.lower()
la = list(a)
lb = list(b)
if la == lb:
    print(0)
else:
    for i in range(len(la)):
        if la[0] == lb[0]:
            del lb[0]
            del la[0]
    lab = [la[0], lb[0]]
    lab_sort = sorted(lab)
    if lab == lab_sort:
        print(-1)
    else:
        print(1)
