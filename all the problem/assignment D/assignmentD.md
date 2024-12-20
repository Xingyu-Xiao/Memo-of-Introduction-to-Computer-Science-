# Assignment #D: 十全十美 

Updated 1254 GMT+8 Dec 17, 2024

2024 fall, Complied by <mark>肖行宇  物院</mark>



**说明：**

1）请把每个题目解题思路（可选），源码Python, 或者C++（已经在Codeforces/Openjudge上AC），截图（包含Accepted），填写到下面作业模版中（推荐使用 typora https://typoraio.cn ，或者用word）。AC 或者没有AC，都请标上每个题目大致花费时间。

2）提交时候先提交pdf文件，再把md或者doc文件上传到右侧“作业评论”。Canvas需要有同学清晰头像、提交文件有pdf、"作业评论"区有上传的md或者doc附件。

3）如果不能在截止前提交作业，请写明原因。



## 1. 题目

### 02692: 假币问题

brute force, http://cs101.openjudge.cn/practice/02692

思路：



代码：

```python
n = int(input())
for _ in range(n):
    lis = {'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L'}
    a = list(input().split())
    b = list(input().split())
    c = list(input().split())
    if a[2] == 'even':
        lis.difference_update(set(a[0]+a[1]))
    if b[2] == 'even':
        lis.difference_update(set(b[0]+b[1]))
    if c[2] == 'even':
        lis.difference_update(set(c[0]+c[1]))
    if a[2] != 'even':
        s = set(a[0]+a[1])
        lis.intersection_update(s)
    if b[2] != 'even':
        s = set(b[0] + b[1])
        lis.intersection_update(s)
    if c[2] != 'even':
        s = set(c[0]+c[1])
        lis.intersection_update(s)
    for ans in lis:
        p = set()
        if a[2] != 'even':
            if a[2] == 'up':
                if ans in a[1]:
                    p.add('light')
                else:
                    p.add('heavy')
            else:
                if ans in a[1]:
                    p.add('heavy')
                else:
                    p.add('light')
        if b[2] != 'even':
            if b[2] == 'up':
                if ans in b[1]:
                    p.add('light')
                else:
                    p.add('heavy')
            else:
                if ans in b[1]:
                    p.add('heavy')
                else:
                    p.add('light')
        if c[2] != 'even':
            if c[2] == 'up':
                if ans in c[1]:
                    p.add('light')
                else:
                    p.add('heavy')
            else:
                if ans in c[1]:
                    p.add('heavy')
                else:
                    p.add('light')
        if len(p) == 1:
            an = ans
            pp = p.pop()
    print(f'{an} is the counterfeit coin and it is {pp}.')

```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![](https://github.com/Xingyu-Xiao/My-Picbed/raw/main/%E5%B1%8F%E5%B9%95%E6%88%AA%E5%9B%BE%202024-12-17%20192329.png)



### 01088: 滑雪

dp, dfs similar, http://cs101.openjudge.cn/practice/01088

思路：

直接dfs，加缓存可以过。

代码：

```python
from functools import lru_cache
r, c = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(r)]
dire = [(-1, 0), (1, 0), (0, -1), (0, 1)]
out = []


@lru_cache(maxsize=None)
def dfs(x, y):
    ans = []
    p = True
    for dx, dy in dire:
        nx, ny = x + dx, y + dy
        if 0 <= nx < r and 0 <= ny < c and arr[nx][ny] < arr[x][y]:
            ans.append(dfs(nx, ny)+1)
            p = False
    if p:
        return 1
    return max(ans)


for i in range(r):
    for j in range(c):
        out.append(dfs(i, j))
print(max(out))

```



代码运行截图 ==（至少包含有"Accepted"）==

![](https://github.com/Xingyu-Xiao/My-Picbed/raw/main/%E5%B1%8F%E5%B9%95%E6%88%AA%E5%9B%BE%202024-12-18%20111725.png)



### 25572: 螃蟹采蘑菇

bfs, dfs, http://cs101.openjudge.cn/practice/25572/

思路：



代码：

```python
from collections import deque

n = int(input())
maze = [list(map(int, input().split())) for _ in range(n)]
dire = ((0, -1), (1, 0), (0, 1), (-1, 0))


def find():
    for i in range(n):
        for j in range(n-1):
            if maze[i][j] == 5 and maze[i][j+1] == 5:
                return ((i, j), True)
    for i in range(n-1):
        for j in range(n):
            if maze[i][j] == 5 and maze[i+1][j] == 5:
                return ((i, j), False)


def bfs1(start):
    queue = deque([start])
    visited = set()
    visited.add(start)
    while queue:
        x, y = queue.popleft()
        for dx, dy in dire:
            nx, ny = x + dx, y + dy
            if (0 <= nx < n) and (0 <= ny < n-1) and (maze[nx][ny] != 1) and ((nx, ny) not in visited) and (maze[nx][ny+1] != 1):
                if maze[nx][ny] == 9 or maze[nx][ny+1] == 9:
                    return 'yes'
                queue.append((nx, ny))
                visited.add((nx, ny))
    return 'no'


def bfs2(start):
    queue = deque([start])
    visited = set()
    visited.add(start)
    while queue:
        x, y = queue.popleft()
        for dx, dy in dire:
            nx, ny = x + dx, y + dy
            if (0 <= nx < n-1) and (0 <= ny < n) and (maze[nx][ny] != 1) and ((nx, ny) not in visited) and (
                    maze[nx+1][ny] != 1):
                if maze[nx][ny] == 9 or maze[nx+1][ny] == 9:
                    return 'yes'
                queue.append((nx, ny))
                visited.add((nx, ny))
    return 'no'


st = find()
if st[1]:
    print(bfs1(st[0]))
else:
    print(bfs2(st[0]))

```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![](https://github.com/Xingyu-Xiao/My-Picbed/raw/main/%E5%B1%8F%E5%B9%95%E6%88%AA%E5%9B%BE%202024-12-19%20173405.png)



### 27373: 最大整数

dp, http://cs101.openjudge.cn/practice/27373/

思路：



代码：

```python
from functools import cmp_to_key
m = int(input())
n = int(input())
s = input().split()


def cmp(a, b):
    if a+b > b+a:
        return 1
    elif a+b < b+a:
        return -1
    else:
        return 0


s.sort(key=cmp_to_key(cmp))
dp = [['' for i in range(m+1)] for j in range(n+1)]
for i in range(1, n+1):
    for j in range(1, m+1):
        if len(s[i-1]) > j:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = str(max(int(dp[i-1][j]) if dp[i-1][j] else 0, int(s[i-1]+dp[i-1][j-len(s[i-1])])))
print(dp[-1][-1])

```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![](https://github.com/Xingyu-Xiao/My-Picbed/raw/main/%E5%B1%8F%E5%B9%95%E6%88%AA%E5%9B%BE%202024-12-20%20150617.png)



### 02811: 熄灯问题

brute force, http://cs101.openjudge.cn/practice/02811

思路：



代码：

```python
from itertools import product
from copy import deepcopy
s = [list(map(int, input().split())) for _ in range(5)]
out = [[0 for _ in range(6)] for _ in range(5)]
dire = [(0, 1), (1, 0), (0, -1), (-1, 0), (0, 0)]
ite = list(product([1, 0], repeat=6))


def change(i, j):
    for dx, dy in dire:
        x, y = i + dx, j + dy
        if 0 <= x < 5 and 0 <= y < 6:
            ss[x][y] = 1 if ss[x][y] == 0 else 0


def extinguish(i):
    for j in range(6):
        if ss[i-1][j] == 1:
            out[i][j] = 1
            change(i, j)
        else:
            out[i][j] = 0


for x in ite:
    ss = deepcopy(s)
    for k in range(6):
        if x[k] == 1:
            change(0, k)
            out[0][k] = 1
        else:
            out[0][k] = 0
    for i in range(1, 5):
        extinguish(i)
    if not any(y == 1 for y in ss[-1]):
        for o in out:
            print(*o)
        break

```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![](https://github.com/Xingyu-Xiao/My-Picbed/raw/main/%E5%B1%8F%E5%B9%95%E6%88%AA%E5%9B%BE%202024-12-18%20101414.png)



### 08210: 河中跳房子

binary search, greedy, http://cs101.openjudge.cn/practice/08210/

思路：



代码：

```python
l, n, m = map(int, input().split())
rock = [0] + [int(input()) for _ in range(n)] + [l]


def check(min_dis):
    num = 0
    j = 0
    for i in range(1, n+2):
        if rock[i] - rock[j] < min_dis:
            num += 1
        else:
            j = i
    if num <= m:
        return True
    else:
        return False


left, right = 0, l+1
while left < right:
    mid = (left + right) // 2
    if check(mid):
        left = mid + 1
        ans = mid
    else:
        right = mid
print(ans)

```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![](https://github.com/Xingyu-Xiao/My-Picbed/raw/main/%E5%B1%8F%E5%B9%95%E6%88%AA%E5%9B%BE%202024-12-20%20165120.png)



## 2. 学习总结和收获

<mark>如果作业题目简单，有否额外练习题目，比如：OJ“计概2024fall每日选做”、CF、LeetCode、洛谷等网站题目。</mark>

主要是复习了一下二分查找，查找的边界有很多细节需要注意。



