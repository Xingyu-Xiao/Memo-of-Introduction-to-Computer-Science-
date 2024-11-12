n = int(input())
s = [(tuple(map(int, input().split()))) for _ in range(n)]
s.sort()
ss = [s[j] for j in range(n-1) if s[j+1][1] >= s[j][1]]
if len(ss) != len(s)-1:
    print("Happy Alex")
else:
    print("Poor Alex")
