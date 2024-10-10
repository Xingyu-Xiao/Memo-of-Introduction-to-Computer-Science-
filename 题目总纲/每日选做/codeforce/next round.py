n, k = input().split()
score = list(input().split())
n, k = int(n), int(k)
for i in range(n):
    score[i] = int(score[i])
score_reverse = list(reversed(score))
p = score[k-1]
q = score_reverse.index(p)
if p != 0:
    print(n-q)
else:
    x = score.index(0)
    print(x)
