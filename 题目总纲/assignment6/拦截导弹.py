n = int(input())
s = list(map(int, input().split()))
max_len = [0]*n
max_len[0] = 1
for i in range(1, n):
    max_len[i] = max(max_len[j]+1 if s[i] <= s[j] else 1 for j in range(i))
print(max(max_len))
