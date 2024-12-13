# Assignment #C: 五味杂陈 

Updated 1148 GMT+8 Dec 10, 2024

2024 fall, Complied by <mark>肖行宇   物理学院</mark>



**说明：**

1）请把每个题目解题思路（可选），源码Python, 或者C++（已经在Codeforces/Openjudge上AC），截图（包含Accepted），填写到下面作业模版中（推荐使用 typora https://typoraio.cn ，或者用word）。AC 或者没有AC，都请标上每个题目大致花费时间。

2）提交时候先提交pdf文件，再把md或者doc文件上传到右侧“作业评论”。Canvas需要有同学清晰头像、提交文件有pdf、"作业评论"区有上传的md或者doc附件。

3）如果不能在截止前提交作业，请写明原因。



## 1. 题目

### 1115. 取石子游戏

dfs, https://www.acwing.com/problem/content/description/1117/

思路：



代码：

```python
def g(a, b):
    if a//b >= 2:
        return 'lose'


def f(a, b):
    if a//b >= 2:
        return 'win'
    else:
        if g(b, a-b):
            return g(b, a-b)
        else:
            return f(a-b, 2*b-a)


while True:
    a, b = map(int, input().split())
    if a == 0 and b == 0:
        break
    if a == b:
        print('win')
        continue
    if a < b:
        a, b = b, a
    print(f(a,b))

```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![](https://github.com/Xingyu-Xiao/My-Picbed/raw/main/%E5%B1%8F%E5%B9%95%E6%88%AA%E5%9B%BE%202024-12-13%20133745.png)



### 25570: 洋葱

Matrices, http://cs101.openjudge.cn/practice/25570

思路：



代码：

```python
n = int(input())
matrix = [list(map(int,input().split())) for _ in range(n)]
ans = []
i, j = 0, n-1
while i < j:
    ans.append(sum(matrix[i][k] for k in range(i, j+1))+sum(matrix[j][k] for k in range(i, j+1))+sum(matrix[k][i] for k in range(i+1, j))+sum(matrix[k][j] for k in range(i+1, j)))
    i += 1
    j -= 1
if n % 2 == 1:
    ans.append(matrix[n//2][n//2])
print(max(ans))
```



代码运行截图 ==（至少包含有"Accepted"）==

![](https://github.com/Xingyu-Xiao/My-Picbed/raw/main/%E5%B1%8F%E5%B9%95%E6%88%AA%E5%9B%BE%202024-12-13%20140720.png)



### 1526C1. Potions(Easy Version)

greedy, dp, data structures, brute force, *1500, https://codeforces.com/problemset/problem/1526/C1

思路：



代码：

```python
import heapq
min_heap = []
n = int(input())
s = list(map(int, input().split()))
health = 0
ans = 0
for x in s:
    health += x
    if x >= 0:
        ans += 1
    else:
        heapq.heappush(min_heap, x)
        if health < 0:
            health -= heapq.heappop(min_heap)
        else:
            ans += 1
print(ans)
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![](https://github.com/Xingyu-Xiao/My-Picbed/raw/main/%E5%B1%8F%E5%B9%95%E6%88%AA%E5%9B%BE%202024-12-13%20154525.png)



### 22067: 快速堆猪

辅助栈，http://cs101.openjudge.cn/practice/22067/

思路：



代码：

```python
min_pig = []
pig = []
while True:
    try:
        s = input()
        if s[0] == 'p':
            if s[1] == 'u':
                top = int(s.split()[1])
                pig.append(top)
                if min_pig:
                    min_pig.append(min(top, min_pig[-1]))
                else:
                    min_pig.append(top)
            if s[1] == 'o':
                if pig:
                    p = pig.pop()
                    if min_pig:
                        min_pig.pop()
        if s[0] == 'm':
            if min_pig:
                print(min_pig[-1])
    except EOFError:
        break
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![](https://github.com/Xingyu-Xiao/My-Picbed/raw/main/%E5%B1%8F%E5%B9%95%E6%88%AA%E5%9B%BE%202024-12-13%20151158.png)



### 20106: 走山路

Dijkstra, http://cs101.openjudge.cn/practice/20106/

思路：



代码：

```python
import heapq
dire = [(0,1),(-1,0),(0,-1),(1,0)]
m, n, p = map(int, input().split())
graph = [input().split() for _ in range(m)]
for i in range(m):
    for j in range(n):
        try:
            graph[i][j] = int(graph[i][j])
        except ValueError:
            continue


def dijkstra(start, end):
    if graph[start[0]][start[1]] == '#':
        return float('inf')
    dist = {(i, j): float('inf') for i in range(m) for j in range(n)}
    queue = [(0, start)]
    dist[start] = 0
    while queue:
        cur_dist, node = heapq.heappop(queue)
        x, y = node
        if cur_dist < dist[node]:
            continue
        for dx, dy in dire:
            nx, ny = x + dx, y + dy
            if 0 <= nx < m and 0 <= ny < n:
                if graph[nx][ny] != '#':
                    new_dist = cur_dist + abs(graph[nx][ny]-graph[x][y])
                    if new_dist < dist[(nx, ny)]:
                        dist[(nx, ny)] = new_dist
                        heapq.heappush(queue, (new_dist, (nx, ny)))
    return dist[end]


for _ in range(p):
    s = list(map(int, input().split()))
    ans = dijkstra((s[0], s[1]), (s[2], s[3]))
    if ans == float('inf'):
        print('NO')
    else:
        print(ans)
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![](https://github.com/Xingyu-Xiao/My-Picbed/raw/main/%E5%B1%8F%E5%B9%95%E6%88%AA%E5%9B%BE%202024-12-13%20163820.png)



### 04129: 变换的迷宫

bfs, http://cs101.openjudge.cn/practice/04129/

思路：



代码：

```python
from collections import deque
dire = [(0,1),(1,0),(0,-1),(-1,0)]


def bfs(i, j):
    queue = deque([(i, j, 0)])
    visited = {(i, j, 0)}
    while queue:
        x, y, n = queue.popleft()
        for dx, dy in dire:
            nx, ny = x + dx, y + dy
            if 0 <= nx < r and 0 <= ny < c and (nx, ny, (n+1) % k) not in visited:
                if maze[nx][ny] == 'E':
                    return n+1
                if (n+1) % k == 0 or maze[nx][ny] != '#':
                    queue.append((nx, ny, n+1))
                    visited.add((nx, ny, (n+1) % k))
    return 'Oop!'


t = int(input())
for _ in range(t):
    r, c, k = map(int, input().split())
    maze = [input() for _ in range(r)]
    p = False
    for i in range(r):
        for j in range(c):
            if maze[i][j] == 'S':
                print(bfs(i, j))
                p = True
                break
        if p:
            break
    p = False

```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![](https://github.com/Xingyu-Xiao/My-Picbed/raw/main/%E5%B1%8F%E5%B9%95%E6%88%AA%E5%9B%BE%202024-12-13%20174106.png)



## 2. 学习总结和收获

<mark>如果作业题目简单，有否额外练习题目，比如：OJ“计概2024fall每日选做”、CF、LeetCode、洛谷等网站题目。</mark>

虽然之前dfs题解一直会给heapq的做法但从来没学，今天为了写Potions和走山路终于学了一下，确实好用。

最后一题没有注意到可以走回起点反复wrong answer，心态爆炸，oj不给测试数据这一点必须批评（.
