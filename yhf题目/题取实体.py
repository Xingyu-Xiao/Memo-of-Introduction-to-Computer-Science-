a = int(input())
s = 0
for i in range(a):
    words = list(input().split())
    q = False
    for word in words:
        if word.startswith('###') and word.endswith('###'):
            if not q:
                s += 1
                q = True
        else:
            q = False
print(s)
