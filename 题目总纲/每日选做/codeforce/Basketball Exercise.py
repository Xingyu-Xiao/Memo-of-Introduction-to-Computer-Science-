n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
dp_1 = [0]*(n+1)
dp_2 = [0]*(n+1)
dp_1[1] = a[0]
dp_2[1] = b[0]
for i in range(1, n+1):
    dp_1[i] = max(dp_2[i-1] + a[i-1], dp_1[i-1])
    dp_2[i] = max(dp_1[i-1] + b[i-1], dp_2[i-1])
print(max(dp_1[-1], dp_2[-1]))
