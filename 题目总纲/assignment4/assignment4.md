# Assignment #4: T-primes + 贪心

Updated 0337 GMT+8 Oct 15, 2024

2024 fall, Complied by <mark>肖行宇 物理学院</mark>



**说明：**

1）请把每个题目解题思路（可选），源码Python, 或者C++（已经在Codeforces/Openjudge上AC），截图（包含Accepted），填写到下面作业模版中（推荐使用 typora https://typoraio.cn ，或者用word）。AC 或者没有AC，都请标上每个题目大致花费时间。

3）课程网站是Canvas平台, https://pku.instructure.com, 学校通知9月19日导入选课名单后启用。**作业写好后，保留在自己手中，待9月20日提交。**

提交时候先提交pdf文件，再把md或者doc文件上传到右侧“作业评论”。Canvas需要有同学清晰头像、提交文件有pdf、"作业评论"区有上传的md或者doc附件。

4）如果不能在截止前提交作业，请写明原因。



## 1. 题目

### 34B. Sale

greedy, sorting, 900, https://codeforces.com/problemset/problem/34/B



思路：



代码

```python
n, m = map(int, input().split())
a = list(map(int, input().split()))
a.sort()
if a[m-1] <= 0:
    print(-sum(a[0:m]))
else:
    s = 0
    for x in a[:m]:
        if x <= 0:
            s += x
    print(-s)

```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![](https://github.com/Xingyu-Xiao/My-Picbed/raw/main/%E5%B1%8F%E5%B9%95%E6%88%AA%E5%9B%BE%202024-10-15%20215340.png)



### 160A. Twins

greedy, sortings, 900, https://codeforces.com/problemset/problem/160/A

思路：



代码

```python
n = int(input())
a = list(map(int, input().split()))
a = sorted(a, reverse=True)
for i in range(n+1):
    if sum(a[:i]) > sum(a[i:]):
        print(i)
        break

```



代码运行截图 ==（至少包含有"Accepted"）==

![](https://github.com/Xingyu-Xiao/My-Picbed/raw/main/%E5%B1%8F%E5%B9%95%E6%88%AA%E5%9B%BE%202024-10-15%20215513.png)



### 1879B. Chips on the Board

constructive algorithms, greedy, 900, https://codeforces.com/problemset/problem/1879/B

思路：



代码

```python
a = int(input())
 
 
def f():
    s = []
    for i in range(3*a):
        s.append(input())
    return s
 
 
b = f()
for i in range(a):
    q = b[3*i:3*i+3]
    n = sum(map(int, q[1].split()))
    nn = sum(map(int, q[2].split()))
    m = int(q[0])*min(map(int, q[2].split()))
    mm = int(q[0])*min(map(int, q[1].split()))
    if n+m < nn+mm:
        print(n+m)
    else:
        print(nn+mm)

```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![](https://github.com/Xingyu-Xiao/My-Picbed/raw/main/%E5%B1%8F%E5%B9%95%E6%88%AA%E5%9B%BE%202024-10-15%20215540.png)



### 158B. Taxi

*special problem, greedy, implementation, 1100, https://codeforces.com/problemset/problem/158/B

思路：



代码

```python
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


```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![](https://github.com/Xingyu-Xiao/My-Picbed/raw/main/%E5%B1%8F%E5%B9%95%E6%88%AA%E5%9B%BE%202024-10-15%20215643.png)



### *230B. T-primes（选做）

binary search, implementation, math, number theory, 1300, http://codeforces.com/problemset/problem/230/B

思路：



代码

```python
n = int(input())
a = list(map(int, input().split()))
r = [True] * (10**6+1)
p = 2
while p*p <= 10**6:
    if r[p]:
        for i in range(p*p, 10**6+1, p):
            r[i] = False
    p += 1
prime = [y for y in range(2, 10**6) if r[y]]
T_prime = set(p*p for p in prime)
result = ['YES' if x in T_prime else 'NO' for x in a]
print('\n'.join(result))

```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![](https://github.com/Xingyu-Xiao/My-Picbed/raw/main/%E5%B1%8F%E5%B9%95%E6%88%AA%E5%9B%BE%202024-10-15%20215715.png)



### *12559: 最大最小整数 （选做）

greedy, strings, sortings, http://cs101.openjudge.cn/practice/12559

思路：



代码

```python
n = int(input())
s = list(input().split())
for i in range(n):
    p = False
    for j in range(n-i-1):
        if s[j] + s[j+1] < s[j+1] + s[j]:
            s[j], s[j+1] = s[j+1], s[j]
            p = True
    if not p:
        break
print(''.join(s), ''.join(reversed(s)))

```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![](https://github.com/Xingyu-Xiao/My-Picbed/raw/main/%E5%B1%8F%E5%B9%95%E6%88%AA%E5%9B%BE%202024-10-16%20112818.png)



## 2. 学习总结和收获

<mark>如果作业题目简单，有否额外练习题目，比如：OJ“计概2024fall每日选做”、CF、LeetCode、洛谷等网站题目。</mark>

T-primes给我收获很大，不光是学会了埃氏筛，更多的是有了预处理的思想，另外发现自己对排序不是很了解，简单的冒泡排序也是看了课件之后才了解。



