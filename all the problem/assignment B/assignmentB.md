# Assignment #B: Dec Mock Exam大雪前一天

Updated 1649 GMT+8 Dec 5, 2024

2024 fall, Complied by <mark>肖行宇  物院</mark>



**说明：**

1）⽉考： AC6<mark>（1）</mark> 。考试题⽬都在“题库（包括计概、数算题目）”⾥⾯，按照数字题号能找到，可以重新提交。作业中提交⾃⼰最满意版本的代码和截图。

2）请把每个题目解题思路（可选），源码Python, 或者C++（已经在Codeforces/Openjudge上AC），截图（包含Accepted），填写到下面作业模版中（推荐使用 typora https://typoraio.cn ，或者用word）。AC 或者没有AC，都请标上每个题目大致花费时间。

3）提交时候先提交pdf文件，再把md或者doc文件上传到右侧“作业评论”。Canvas需要有同学清晰头像、提交文件有pdf、"作业评论"区有上传的md或者doc附件。

4）如果不能在截止前提交作业，请写明原因。



## 1. 题目

### E22548: 机智的股民老张

http://cs101.openjudge.cn/practice/22548/

思路：



代码：

```python
a = list(map(int, input().split()))
ans = 0
s = [(x, i) for i, x in enumerate(a)]
s.sort()
for i in range(len(s)):
    for j in range(len(s)-1,i,-1):
        if s[j][1] > s[i][1]:
            ans = max(ans,s[j][0] - s[i][0])
            break
print(ans)
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![](https://github.com/Xingyu-Xiao/My-Picbed/raw/main/%E5%B1%8F%E5%B9%95%E6%88%AA%E5%9B%BE%202024-12-05%20174506.png)



### M28701: 炸鸡排

greedy, http://cs101.openjudge.cn/practice/28701/

思路：



代码：

```python
n, k = map(int, input().split())
a = list(map(int, input().split()))
sum_a = sum(a)
a.sort()
for i in range(n):
    if a[-1] > sum_a/k:
        k -= 1
        sum_a -= a.pop()
    else:
        print(f'{sum_a/k:.3f}')
        break
```



代码运行截图 ==（至少包含有"Accepted"）==

![](https://github.com/Xingyu-Xiao/My-Picbed/raw/main/%E5%B1%8F%E5%B9%95%E6%88%AA%E5%9B%BE%202024-12-05%20210332.png)



### M20744: 土豪购物

dp, http://cs101.openjudge.cn/practice/20744/

思路：



代码：

```python
s = list(map(int, input().split(',')))
dp1 = [0]*len(s)
dp2 = [0]*len(s)
dp1[0] = s[0]
dp2[0] = s[0]
for i in range(1, len(s)):
    dp1[i] = max(s[i], s[i]+dp1[i-1])
    dp2[i] = max(dp1[i], dp1[i-1], dp2[i-1]+s[i], s[i])
print(max(dp2))
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![](https://github.com/Xingyu-Xiao/My-Picbed/raw/main/%E5%B1%8F%E5%B9%95%E6%88%AA%E5%9B%BE%202024-12-05%20214054.png)



### T25561: 2022决战双十一

brute force, dfs, http://cs101.openjudge.cn/practice/25561/

思路：



代码：

```python
n, m = map(int, input().split())
sp = [[tuple(map(int, x.split(':'))) for x in input().split()] for _ in range(n)]
qx = [[tuple(map(int, x.split('-'))) for x in input().split()] for _ in range(m)]
loop = []


def nested_loops(n, current=0, res=None):
    if not res:
        res = ['']*n
    if current == n:
        loop.append(res.copy())
        return
    for s_p in sp[current]:
        res[current] = s_p
        nested_loops(n, current + 1, res)


nested_loops(n)
ans = float('inf')
for loo in loop:
    shop = [0]*m
    price = 0
    for lo in loo:
        price += lo[1]
        shop[lo[0]-1] += lo[1]
    price -= 50*(price//300)
    for i, pr in enumerate(shop):
        q_x = qx[i]
        q_x.sort(key=lambda x: -x[1])
        for q, x in q_x:
            if pr >= q:
                price -= x
                break
    ans = min(ans, price)
print(ans)

```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![](https://github.com/Xingyu-Xiao/My-Picbed/raw/main/%E5%B1%8F%E5%B9%95%E6%88%AA%E5%9B%BE%202024-12-05%20205405.png)



### T20741: 两座孤岛最短距离

dfs, bfs, http://cs101.openjudge.cn/practice/20741/

思路：



代码：

```python
from collections import deque
n = int(input())
s = [list(input()) for _ in range(n)]
dire = [(1, 0), (-1, 0), (0, 1), (0, -1)]


def f():
    a = set()
    for i in range(n):
        for j in range(n):
            if s[i][j] == '1':
                s[i][j] = '-1'
                queue = deque([(i, j)])
                a.add((i, j))
                while queue:
                    x, y = queue.popleft()
                    for dx, dy in dire:
                        nx, ny = x + dx, y + dy
                        if 0 <= nx < n and 0 <= ny < n:
                            if s[nx][ny] == '1':
                                queue.append((nx, ny))
                                s[nx][ny] = '-1'
                            elif s[nx][ny] == '0':
                                a.add((x, y))
                return a


ans = float('inf')
island1 = f()
island2 = f()
for x in island1:
    for y in island2:
        i, j = x
        k, p = y
        ans = min(ans, abs(i-k)+abs(j-p)-1)
print(ans)

```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![](https://github.com/Xingyu-Xiao/My-Picbed/raw/main/%E5%B1%8F%E5%B9%95%E6%88%AA%E5%9B%BE%202024-12-05%20183008.png)



### T28776: 国王游戏

greedy, http://cs101.openjudge.cn/practice/28776

思路：



代码：

```python
n = int(input())
a, b = map(int, input().split())
s = [tuple(map(int, input().split())) for _ in range(n)]
s.sort(key=lambda x: x[0]*x[1])
ans = [0]*n
ans[0] = a
for i in range(1, n):
    ans[i] = ans[i-1]*s[i-1][0]
print(max(ans[i]//s[i][1] for i in range(n)))
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![](https://github.com/Xingyu-Xiao/My-Picbed/raw/main/%E5%B1%8F%E5%B9%95%E6%88%AA%E5%9B%BE%202024-12-05%20192522.png)



## 2. 学习总结和收获

<mark>如果作业题目简单，有否额外练习题目，比如：OJ“计概2024fall每日选做”、CF、LeetCode、洛谷等网站题目。</mark>

唉，这次考试挺难的，贪心题一下子没思路的话就要卡好久，吃完饭后一直做也9点多才写完。而且这次可能因为第一题easy就卡了一下，导致后面整个人都比较慌没什么状态，每个题都试着做一下但都没AC。



