a, b = input().split()
M = int(a)
N = int(b)
if M % 2 == 0 or N % 2 == 0:
    print(int(M*N/2))
else:
    x = N//2
    y = (M-1)*N/2
    print(int(x+y))
