# Assignment #6: Recursion and DP

Updated 2201 GMT+8 Oct 29, 2024

2024 fall, Complied by <mark>肖行宇  物理学院</mark>



**说明：**

1）请把每个题目解题思路（可选），源码Python, 或者C++（已经在Codeforces/Openjudge上AC），截图（包含Accepted），填写到下面作业模版中（推荐使用 typora https://typoraio.cn ，或者用word）。AC 或者没有AC，都请标上每个题目大致花费时间。

3）提交时候先提交pdf文件，再把md或者doc文件上传到右侧“作业评论”。Canvas需要有同学清晰头像、提交文件有pdf、"作业评论"区有上传的md或者doc附件。

4）如果不能在截止前提交作业，请写明原因。



## 1. 题目

### sy119: 汉诺塔

recursion, https://sunnywhy.com/sfbj/4/3/119  

思路：



代码：

```python
def num(n):
    if n == 1:
        return 1
    else:
        return 2*num(n-1) + 1


def move_one(ori, aim):
    print(f'{ori}->{aim}')


def move(n, a, b, c):
    if n == 1:
        move_one(a, c)
    else:
        move(n-1, a, c, b)
        move_one(a, c)
        move(n-1, b, a, c)


k = int(input())
print(num(k))
move(k, 'A', 'B', 'C')
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![](https://github.com/Xingyu-Xiao/My-Picbed/raw/main/%E5%B1%8F%E5%B9%95%E6%88%AA%E5%9B%BE%202024-10-30%20183211.png)



### sy132: 全排列I

recursion, https://sunnywhy.com/sfbj/4/3/132

思路：



代码：

```python
p = [False]*9


def f(n, tem=[]):
    if len(tem) == n:
        return [tem]
    else:
        out = []
        for i in range(1, n+1):
            if p[i]:
                continue
            else:
                p[i] = True
                out.extend(f(n, tem+[i]))
                p[i] = False
        return out


for x in f(int(input())):
    print(*x)
```



代码运行截图 ==（至少包含有"Accepted"）==

![](https://github.com/Xingyu-Xiao/My-Picbed/raw/main/%E5%B1%8F%E5%B9%95%E6%88%AA%E5%9B%BE%202024-10-30%20220611.png)



### 02945: 拦截导弹 

dp, http://cs101.openjudge.cn/2024fallroutine/02945

思路：



代码：

```python
n = int(input())
s = list(map(int, input().split()))
max_len = [0]*n
max_len[0] = 1
for i in range(1, n):
    max_len[i] = max(max_len[j]+1 if s[i] <= s[j] else 1 for j in range(i))
print(max(max_len))
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![](https://github.com/Xingyu-Xiao/My-Picbed/raw/main/%E5%B1%8F%E5%B9%95%E6%88%AA%E5%9B%BE%202024-10-30%20163955.png)



### 23421: 小偷背包 

dp, http://cs101.openjudge.cn/practice/23421

思路：



代码：

```python
n, b = map(int, input().split())
price = list(map(int, input().split()))
weight = list(map(int, input().split()))
dp = [0]*(b+1)
for i in range(n):
    for j in range(b, weight[i]-1, -1):
        dp[j] = max(dp[j], price[i]+dp[j-weight[i]])
print(dp[-1])

```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![](https://github.com/Xingyu-Xiao/My-Picbed/raw/main/%E5%B1%8F%E5%B9%95%E6%88%AA%E5%9B%BE%202024-10-31%20093923.png)



### 02754: 八皇后

dfs and similar, http://cs101.openjudge.cn/practice/02754

思路：



代码：

```python
ans = []
a = [None for i in range(9)]


def f(t=1):
    if t == 9:
        ans.append(''.join(map(str, a[1:])))
    else:
        for j in range(1, 9):
            for i in range(1, t):
                if j == a[i] or abs(t-i) == abs(j-a[i]):
                    break
            else:
                a[t] = j
                f(t+1)


f()
for i in range(int(input())):
    print(ans[int(input())-1])

```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![](https://github.com/Xingyu-Xiao/My-Picbed/raw/main/%E5%B1%8F%E5%B9%95%E6%88%AA%E5%9B%BE%202024-10-30%20230204.png)



### 189A. Cut Ribbon 

brute force, dp 1300 https://codeforces.com/problemset/problem/189/A

思路：



代码：

```python
def m_ax(x):
    n, a, b, c = x
    dp = [-1]*(n+1)
    dp[0] = 0
    for i in range(min(a, b, c), n+1):
        add_a = dp[i-a] + 1 if i >= a and dp[i-a] >= 0 else -1
        add_b = dp[i-b] + 1 if i >= b and dp[i-b] >= 0 else -1
        add_c = dp[i-c] + 1 if i >= c and dp[i-c] >= 0 else -1
        dp[i] = max(add_a, add_b, add_c)
    return dp[-1]


print(m_ax(map(int, input().split())))
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>





## 2. 学习总结和收获

<mark>如果作业题目简单，有否额外练习题目，比如：OJ“计概2024fall每日选做”、CF、LeetCode、洛谷等网站题目。</mark>

感觉这次的题目很有难度，基本上没有自己做出来的，全靠看答案（悲



