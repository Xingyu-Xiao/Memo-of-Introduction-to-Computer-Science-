a = int(input())
x = a//100
a = a - 100 * x
y = a//20
a = a - 20 * y
z = a//10
a = a - 10 * z
n = a//5
a = a % 5
print(x+y+z+n+a)
