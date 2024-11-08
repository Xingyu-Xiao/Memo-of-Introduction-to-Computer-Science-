a = list(map(int, input().split()))
n = a[0]
k = a[1]
l = a[2]
c = a[3]
d = a[4]
nl = a[6]
p = a[5]
np = a[7]
print(min([c*d//n, k*l//(nl*n), p//(np*n)]))
