n = int(input())
s = list(map(int, input().split()))
s.sort()
i = 0
wait = 0
for x in s:
    if x >= wait:
        i += 1
        wait += x
print(i)
