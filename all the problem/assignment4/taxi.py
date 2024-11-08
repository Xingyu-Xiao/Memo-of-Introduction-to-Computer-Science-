import math
n = int(input())
s = list(map(int, input().split()))
n_1 = s.count(1)
n_2 = s.count(2)
n_3 = s.count(3)
n_4 = s.count(4)
if n_3 >= n_1:
    print(n_4+n_3+math.ceil(n_2/2))
else:
    if n_2 % 2 == 0:
        print(n_4+n_3+math.ceil((n_1-n_3)/4)+n_2//2)
    else:
        print(n_4+n_3+math.ceil((n_1-n_3-2)/4)+n_2//2+1)
