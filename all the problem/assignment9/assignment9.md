# Assignment #9: dfs, bfs, & dp

Updated 2107 GMT+8 Nov 19, 2024

2024 fall, Complied by <mark>肖行宇  物理学院</mark>



**说明：**

1）请把每个题目解题思路（可选），源码Python, 或者C++（已经在Codeforces/Openjudge上AC），截图（包含Accepted），填写到下面作业模版中（推荐使用 typora https://typoraio.cn ，或者用word）。AC 或者没有AC，都请标上每个题目大致花费时间。

2）提交时候先提交pdf文件，再把md或者doc文件上传到右侧“作业评论”。Canvas需要有同学清晰头像、提交文件有pdf、"作业评论"区有上传的md或者doc附件。

3）如果不能在截止前提交作业，请写明原因。



## 1. 题目

### 18160: 最大连通域面积

dfs similar, http://cs101.openjudge.cn/practice/18160

思路：bfs



代码：

```python
from collections import deque


def bfs(s, n, m, i, j):
    queue = deque([(i, j)])
    con = 0
    while queue:
        x, y = queue.popleft()
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                if 0 <= x + dx < n and 0 <= y + dy < m:
                    if s[x + dx][y + dy] == 'W':
                        queue.append((x + dx, y + dy))
                        con += 1
                        s[x + dx][y + dy] = '.'
    return con


t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    s = [list(input()) for _ in range(n)]
    ans = 0
    for i in range(n):
        for j in range(m):
            if s[i][j] == 'W':
                ans = max(ans, bfs(s, n, m, i, j))
    print(ans)
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![](https://github.com/Xingyu-Xiao/My-Picbed/raw/main/%E5%B1%8F%E5%B9%95%E6%88%AA%E5%9B%BE%202024-11-20%20151327.png)



### 19930: 寻宝

bfs, http://cs101.openjudge.cn/practice/19930

思路：

bfs

代码：

```python
from collections import deque
n, m = map(int, input().split())
s = [list(map(int, input().split())) for _ in range(n)]
if s[0][0] == 1:
    print(0)
else:
    queue = deque([(0, 0)])
    visited = set()
    visited.add((0, 0))
    next_point = ((1, 0), (0, -1), (0, 1), (-1, 0))
    ans = 0
    p = True
    while True:
        new_queue = deque()
        while queue:
            x, y = queue.popleft()
            for dx, dy in next_point:
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < m:
                    if s[nx][ny] == 0:
                        if (nx, ny) not in visited:
                            new_queue.append((nx, ny))
                            visited.add((nx, ny))
                    elif s[nx][ny] == 1:
                        p = False
                        break
            if not p:
                break
        queue = new_queue
        ans += 1
        if not p:
            print(ans)
            break
        if not queue:
            print('NO')
            break

```



代码运行截图 ==（至少包含有"Accepted"）==

![](https://github.com/Xingyu-Xiao/My-Picbed/raw/main/%E5%B1%8F%E5%B9%95%E6%88%AA%E5%9B%BE%202024-11-20%20162635.png)



### 04123: 马走日

dfs, http://cs101.openjudge.cn/practice/04123

思路：



代码：

```python
direction = ((1, 2), (1, -2), (-1, 2), (-1, -2), (2, -1), (2, 1), (-2, 1), (-2, -1))


def solve(n, m, x, y):
    ans = 0
    visited = [[False for _ in range(m)] for _ in range(n)]
    visited[x][y] = True

    def dfs(start, dep=1):
        nonlocal ans
        if dep == n*m:
            ans += 1
            return
        for dx, dy in direction:
            nx, ny = start[0] + dx, start[1] + dy
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
                visited[nx][ny] = True
                dfs((nx, ny), dep+1)
                visited[nx][ny] = False
    dfs((x, y))
    return ans


t = int(input())
for _ in range(t):
    n, m, x, y = map(int, input().split())
    print(solve(n, m, x, y))

```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![](https://github.com/Xingyu-Xiao/My-Picbed/raw/main/%E5%B1%8F%E5%B9%95%E6%88%AA%E5%9B%BE%202024-11-20%20184448.png)



### sy316: 矩阵最大权值路径

dfs, https://sunnywhy.com/sfbj/8/1/316

思路：

dfs,回溯

代码：

```python
n, m = map(int, input().split())
s = [list(map(int, input().split())) for _ in range(n)]
visited = [[True for _ in range(m)] for _ in range(n)]
max_path = []
max_sum = float('-inf')
visited[0][0] = False


def dfs(start, c_sum, c_path):
    global max_path, max_sum
    if start == (n-1, m-1):
        if c_sum > max_sum:
            max_sum = c_sum
            max_path = c_path.copy()
        return
    for dx, dy in ((-1, 0), (1, 0), (0, -1), (0, 1)):
        nx, ny = start[0] + dx, start[1] + dy
        if 0 <= nx < n and 0 <= ny < m and visited[nx][ny]:
            visited[nx][ny] = False
            c_path.append((nx, ny))
            dfs((nx, ny), c_sum + s[nx][ny], c_path)
            visited[nx][ny] = True
            c_path.pop()


dfs((0, 0), s[0][0], [(0, 0)])
for path in max_path:
    print(path[0]+1, path[1]+1)

```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![](https://github.com/Xingyu-Xiao/My-Picbed/raw/main/%E5%B1%8F%E5%B9%95%E6%88%AA%E5%9B%BE%202024-11-20%20181247.png)





### LeetCode62.不同路径

dp, https://leetcode.cn/problems/unique-paths/

思路：



代码：

```python
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0 for _ in range(n+1)] for _ in range(m+1)]
        dp[1][0] = 1
        for i in range(1, m+1):
            for j in range(1, n+1):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return(dp[-1][-1])

```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![](https://github.com/Xingyu-Xiao/My-Picbed/raw/main/%E5%B1%8F%E5%B9%95%E6%88%AA%E5%9B%BE%202024-11-20%20162855.png)



### sy358: 受到祝福的平方

dfs, dp, https://sunnywhy.com/sfbj/8/3/539

思路：

dfs

代码：

```python
import math

a = input()
s = set([i**2 for i in range(1, int(math.sqrt(int(a)))+1)])
ans = []


def f(i=0, j=0):
    while i < len(a) and j < len(a):
        if int(a[i:j+1]) in s:
            f(i, j+1)
            i = j+1
            j = i
        else:
            j += 1
    if j == i:
        ans.append(0)
    return 


f()
if ans:
    print('Yes')
else:
    print('No')
    
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![](https://github.com/Xingyu-Xiao/My-Picbed/raw/main/%E5%B1%8F%E5%B9%95%E6%88%AA%E5%9B%BE%202024-11-20%20171539.png)



## 2. 学习总结和收获

<mark>如果作业题目简单，有否额外练习题目，比如：OJ“计概2024fall每日选做”、CF、LeetCode、洛谷等网站题目。</mark>

回溯还是不太会用，矩阵最大权值路径那题花的时间比较久。

每天一道每日选做果然还是有点少了呢:wink:,现在会写Leetcode每天推的每日一题补成两道:yum:。



