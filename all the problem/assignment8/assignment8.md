# Assignment #8: 田忌赛马来了

Updated 1021 GMT+8 Nov 12, 2024

2024 fall, Complied by <mark>肖行宇  物理学院</mark>



**说明：**

1）请把每个题目解题思路（可选），源码Python, 或者C++（已经在Codeforces/Openjudge上AC），截图（包含Accepted），填写到下面作业模版中（推荐使用 typora https://typoraio.cn ，或者用word）。AC 或者没有AC，都请标上每个题目大致花费时间。

2）提交时候先提交pdf文件，再把md或者doc文件上传到右侧“作业评论”。Canvas需要有同学清晰头像、提交文件有pdf、"作业评论"区有上传的md或者doc附件。

3）如果不能在截止前提交作业，请写明原因。



## 1. 题目

### 12558: 岛屿周⻓

matices, http://cs101.openjudge.cn/practice/12558/ 

思路：



代码：

```python
n, m = map(int, input().split())
s = [[0 for _ in range(m+2)]]+[[0]+list(map(int, input().split()))+[0] for _ in range(n)]+[[0 for _ in range(m+2)]]


def number(i, j):
    num = 0
    if s[i][j+1] == 0:
        num += 1
    if s[i][j-1] == 0:
        num += 1
    if s[i+1][j] == 0:
        num += 1
    if s[i-1][j] == 0:
        num += 1
    return num


ans = 0
for i in range(1, n+1):
    for j in range(1, m+1):
        if s[i][j] == 1:
            ans += number(i, j)
print(ans)
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![](https://github.com/Xingyu-Xiao/My-Picbed/raw/main/%E5%B1%8F%E5%B9%95%E6%88%AA%E5%9B%BE%202024-11-12%20203359.png)



### LeetCode54.螺旋矩阵

matrice, https://leetcode.cn/problems/spiral-matrix/

与OJ这个题目一样的 18106: 螺旋矩阵，http://cs101.openjudge.cn/practice/18106

思路：



代码：

```python
out = []


def f(matrix):
    if matrix:
        m = len(matrix)
        n = len(matrix[0])
        for i in range(n):
            out.append(matrix[0][i])
        if m > 1:
            for j in range(1, m):
                out.append(matrix[j][n - 1])
            if n == 1:
                return
            for k in range(n-2, -1, -1):
                out.append(matrix[m-1][k])
        if m == 1 or m == 2:
            return
        for b in range(m-2, 0, -1):
            out.append(matrix[b][0])
        if n == 2:
            return
        new_matrix = [[matrix[i][j] for j in range(1, n-1)] for i in range(1, m-1)]
        f(new_matrix)
    else:
        return

```



代码运行截图 ==（至少包含有"Accepted"）==

![](https://github.com/Xingyu-Xiao/My-Picbed/raw/main/%E5%B1%8F%E5%B9%95%E6%88%AA%E5%9B%BE%202024-11-12%20195848.png)



### 04133:垃圾炸弹

matrices, http://cs101.openjudge.cn/practice/04133/

思路：



代码：

```python
d = int(input())
n = int(input())
s = {}
for _ in range(n):
    x, y, i = map(int, input().split())
    up = min(y+d, 1024)
    down = max(y-d, 0)
    left = max(x-d, 0)
    right = min(x+d, 1024)
    for k in range(left, right+1):
        for l in range(down, up+1):
            s[(k, l)] = s.get((k, l), 0) + i
out_max = 0
out_num = 1
for location in s.values():
    if out_max == location:
        out_num += 1
    elif out_max < location:
        out_max = location
        out_num = 1
print(out_num, out_max)
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![](https://github.com/Xingyu-Xiao/My-Picbed/raw/main/%E5%B1%8F%E5%B9%95%E6%88%AA%E5%9B%BE%202024-11-12%20203449.png)



### LeetCode376.摆动序列

greedy, dp, https://leetcode.cn/problems/wiggle-subsequence/

与OJ这个题目一样的，26976:摆动序列, http://cs101.openjudge.cn/routine/26976/

思路：



代码：

```python
class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        def solution(nums):
            if len(nums) == 0:
                return 0
            if len(nums) == 1:
                return 1
            length = 2
            last = nums[1]
            if nums[1] - nums[0] > 0:
                p = True
            elif nums[1] - nums[0] < 0:
                p = False
            else:
                return solution(nums[1:])
            for x in nums[2:]:
                if p:
                    if x - last < 0:
                        length += 1
                        p = False
                else:
                    if x - last > 0:
                        length += 1
                        p = True
                last = x
            return length
        return solution(nums)

```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![](https://github.com/Xingyu-Xiao/My-Picbed/raw/main/%E5%B1%8F%E5%B9%95%E6%88%AA%E5%9B%BE%202024-11-12%20200234.png)



### CF455A: Boredom

dp, 1500, https://codeforces.com/contest/455/problem/A

思路：



代码：

```python
import sys
n = int(input())
a = list(map(int, input().split()))
m = max(a)
s = [0]*(m+1)
for x in a:
    s[x] += 1
if m == 1:
    print(s[1])
    sys.exit()
if m == 2:
    print(max(s[2], 2*s[1]))
    sys.exit()
dp = [0]*(m+1)
dp[-1] = m*s[-1]
dp[-2] = max((m-1)*s[-2], m*s[-1])
for i in range(m-2, 0, -1):
    dp[i] = max(dp[i+1], dp[i+2] + i*s[i])
print(dp[1])
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![](https://github.com/Xingyu-Xiao/My-Picbed/raw/main/%E5%B1%8F%E5%B9%95%E6%88%AA%E5%9B%BE%202024-11-12%20200418.png)



### 02287: Tian Ji -- The Horse Racing

greedy, dfs http://cs101.openjudge.cn/practice/02287

思路：



代码：

```python
while 1:
    n = int(input())
    if not n:
        break
    tian = list(map(int, input().split()))
    kings = list(map(int, input().split()))
    kings.sort()
    tian.sort()
    i = j = 0
    k = m = n-1
    ans = 0
    while i <= k:
        if tian[i] > kings[j]:
            ans += 200
            i += 1
            j += 1
        elif tian[k] > kings[m]:
            ans += 200
            k -= 1
            m -= 1
        else:
            if tian[i] < kings[m]:
                ans -= 200
            i += 1
            m -= 1
    print(ans)

```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![](https://github.com/Xingyu-Xiao/My-Picbed/raw/main/%E5%B1%8F%E5%B9%95%E6%88%AA%E5%9B%BE%202024-11-12%20213322.png)



## 2. 学习总结和收获

<mark>如果作业题目简单，有否额外练习题目，比如：OJ“计概2024fall每日选做”、CF、LeetCode、洛谷等网站题目。</mark>

田忌赛马平局的情况不太好考虑清楚，折腾了好久:cry:



