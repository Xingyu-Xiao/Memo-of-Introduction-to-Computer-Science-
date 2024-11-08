from sys import stdin


def max_beautiful_segments(n, a):
    prefix_sum = 0
    prefix_map = set()
    prefix_map.add(0)
    count = 0
    for i in range(1, n+1):
        prefix_sum += a[i-1]
        if prefix_sum in prefix_map:
            count += 1
            prefix_map.clear()
            prefix_map.add(0)
            prefix_sum = 0
        else:
            prefix_map.add(prefix_sum)
    return count


t = int(input())
output = []
for _ in range(t):
    n = int(input())
    a = list(map(int, stdin.readline().strip().split()))
    output.append(max_beautiful_segments(n, a))
print('\n'.join(map(str, output)))
