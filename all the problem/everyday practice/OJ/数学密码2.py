a = int(input())
for i in range(a//6, 0, -1):
    if a % i == 0:
        print(i)
        break
