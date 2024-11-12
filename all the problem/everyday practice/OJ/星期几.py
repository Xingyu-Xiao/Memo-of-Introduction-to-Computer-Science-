a = int(input())
s = []
day = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
for i in range(a):
    s.append(input())
for x in s:
    if int(x[-4:-2]) > 2:
        c = int(x[0:2])
        d = int(x[-2:])
        m = int(x[-4:-2])
        y = int(x[2:4])
    else:
        x = str(int(x)-10000)
        c = int(x[0:2])
        d = int(x[-2:])
        m = int(x[-4:-2])+12
        y = int(x[2:4])
    w = (y + y//4 + c//4 - 2*c + int(26*(m+1)/10) + d - 1) % 7
    print(day[w])
