# Assignment #10: dp & bfs

Updated 2 GMT+8 Nov 25, 2024

2024 fall, Complied by <mark>肖行宇  物院</mark>



**说明：**

1）请把每个题目解题思路（可选），源码Python, 或者C++（已经在Codeforces/Openjudge上AC），截图（包含Accepted），填写到下面作业模版中（推荐使用 typora https://typoraio.cn ，或者用word）。AC 或者没有AC，都请标上每个题目大致花费时间。

2）提交时候先提交pdf文件，再把md或者doc文件上传到右侧“作业评论”。Canvas需要有同学清晰头像、提交文件有pdf、"作业评论"区有上传的md或者doc附件。

3）如果不能在截止前提交作业，请写明原因。



## 1. 题目

### LuoguP1255 数楼梯

dp, bfs, https://www.luogu.com.cn/problem/P1255

思路：



代码：

```python
n = int(input())
dp = [0]*n
if n > 2:
    dp[0] = 1
    dp[1] = 2
    for i in range(2, n):
        dp[i] = dp[i-1] + dp[i-2]
    print(dp[-1])
if (n == 1) or (n == 2):
    print(n)

```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![](https://github.com/Xingyu-Xiao/My-Picbed/raw/main/%E5%B1%8F%E5%B9%95%E6%88%AA%E5%9B%BE%202024-11-27%20151700.png)



### 27528: 跳台阶

dp, http://cs101.openjudge.cn/practice/27528/

思路：



代码：

```python
n = int(input())
if n == 1:
    print(1)
else:
    dp = [0]*n
    dp[0] = 1
    for i in range(1, n):
        dp[i] = sum(dp[:i]) + 1
    print(dp[-1])
    
```



代码运行截图 ==（至少包含有"Accepted"）==

![](https://github.com/Xingyu-Xiao/My-Picbed/raw/main/%E5%B1%8F%E5%B9%95%E6%88%AA%E5%9B%BE%202024-11-27%20152116.png)



### 474D. Flowers

dp, https://codeforces.com/problemset/problem/474/D

思路：



代码：

```python
from sys import stdin
MOD = 10 ** 9 + 7
data = stdin.readlines()
ans = []
result = [0]*100001
t, k = map(int, data[0].strip().split())
dp = [0]*100001
for i in range(k):
    dp[i] = 1
for i in range(k, 100001):
    dp[i] = (dp[i-1] + dp[i-k]) % MOD
for i in range(100001):
    result[i] = result[i-1] + dp[i]
for line in data[1:]:
    a, b = map(int, line.strip().split())
    ans.append((result[b]-result[a-1]) % MOD)
print('\n'.join(map(str, ans)))

```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![](https://github.com/Xingyu-Xiao/My-Picbed/raw/main/%E5%B1%8F%E5%B9%95%E6%88%AA%E5%9B%BE%202024-11-27%20160424.png)



### LeetCode5.最长回文子串

dp, two pointers, string, https://leetcode.cn/problems/longest-palindromic-substring/

思路：



代码：

```python
class Solution:
    def longestPalindrome(self, s: str) -> str:
        ss = '#' + '#'.join(s) + '#'
        radius = [0]*len(ss)
        m = r = max_i = 0
        for i in range(len(ss)):
            radius[i] = min(radius[m]-i+m, radius[2*m-i])
            lf, ri = i-radius[i]-1, i+radius[i]+1
            while lf >= 0 and ri < len(ss) and ss[lf] == ss[ri]:
                lf -= 1
                ri += 1
                radius[i] += 1
            if ri > r:
                r = ri
                m = i
            if radius[i] > radius[max_i]:
                max_i = i
        return ''.join(ss[max_i-radius[max_i]:max_i+radius[max_i]+1].split('#'))


if __name__ == '__main__':
    sol = Solution()
    print(sol.longestPalindrome(input()))

```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![](https://github.com/Xingyu-Xiao/My-Picbed/raw/main/%E5%B1%8F%E5%B9%95%E6%88%AA%E5%9B%BE%202024-11-26%20212507.png)





### 12029: 水淹七军

bfs, dfs, http://cs101.openjudge.cn/practice/12029/

思路：



代码：

```python
import sys
sys.setrecursionlimit(20000)
ss = sys.stdin.read().split()
direction = [(1, 0),(0,1),(-1,0),(0,-1)]


def flood(x, y, s, m, n, v):
    v.add((x, y))
    for dx, dy in direction:
        nx, ny = x + dx, y + dy
        if 0 <= nx < m and 0 <= ny < n and (nx, ny) not in v:
            if s[nx][ny] < s[x][y]:
                s[nx][ny] = s[x][y]
                flood(nx, ny, s, m, n, v)


k = int(ss[0])
idx = 1
for _ in range(k):
    m, n = map(int, ss[idx: idx+2])
    idx += 2
    s = []
    for _ in range(m):
        s.append(list(map(int, ss[idx: idx+n])))
        idx += n
    i, j = map(int, ss[idx: idx+2])
    idx += 2
    origin = s[i-1][j-1]
    p = int(ss[idx])
    idx += 1
    points = []
    for _ in range(p):
        points.append(tuple(map(int, ss[idx: idx+2])))
        idx += 2
    for x, y in points:
        v = set()
        flood(x-1, y-1, s, m, n, v)
    if s[i-1][j-1] == origin:
        print('No')
    else:
        print('Yes')

```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![](https://github.com/Xingyu-Xiao/My-Picbed/raw/main/%E5%B1%8F%E5%B9%95%E6%88%AA%E5%9B%BE%202024-11-26%20194352.png)



### 02802: 小游戏

bfs, http://cs101.openjudge.cn/practice/02802/

思路：



代码：

```python
from collections import deque
dire = [(1, 0), (-1, 0), (0, 1), (0, -1)]


def bfs(x, y, board, goal):
    ans = []
    visited = set()
    queue = deque([(x, y, -1, 0)])
    while queue:
        x, y, d, num = queue.popleft()
        for i, (dx, dy) in enumerate(dire):
            nx, ny = x + dx, y + dy
            new_num = num if i == d else num + 1
            if [ny, nx] == goal:
                ans.append(new_num)
                continue
            if (0 <= nx < len(board) and 0 <= ny < len(board[0]) and (nx, ny, i) not in visited and
                    board[nx][ny] != 'X'):
                visited.add((nx, ny, i))
                queue.append((nx, ny, i, new_num))
    return min(ans, default=None)


n = 0
while True:
    n += 1
    w, h = map(int, input().split())
    if w == h == 0:
        break
    bo = [' '*(w+2)]+[' '+input()+' ' for _ in range(h)]+[' '*(w+2)]
    print(f'Board #{n}:')
    m = 0
    while True:
        m += 1
        card = list(map(int, input().split()))
        if card == [0, 0, 0, 0]:
            break
        ca1 = card[0:2]
        ca2 = card[2:]
        k = bfs(ca1[1], ca1[0], bo, ca2)
        if k:
            print(f'Pair {m}: {k} segments.')
        else:
            print(f'Pair {m}: impossible.')
    print()
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![](https://github.com/Xingyu-Xiao/My-Picbed/raw/main/%E5%B1%8F%E5%B9%95%E6%88%AA%E5%9B%BE%202024-11-27%20110437.png)



## 2. 学习总结和收获

<mark>如果作业题目简单，有否额外练习题目，比如：OJ“计概2024fall每日选做”、CF、LeetCode、洛谷等网站题目。</mark>

水淹七军是不是输入数据乱掉了啊，我用sys.stdin.readlines读取再一行一行匹配也会runtime error.

这次作业花的时间有点多，回文子串Manacher算法看了很久，小游戏细节好多，折腾许久。



