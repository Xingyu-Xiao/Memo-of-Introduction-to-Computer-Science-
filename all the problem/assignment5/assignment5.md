# Assignment #5: Greedy穷举Implementation

Updated 1939 GMT+8 Oct 21, 2024

2024 fall, Complied by <mark>肖行宇 物理学院</mark>



**说明：**

1）请把每个题目解题思路（可选），源码Python, 或者C++（已经在Codeforces/Openjudge上AC），截图（包含Accepted），填写到下面作业模版中（推荐使用 typora https://typoraio.cn ，或者用word）。AC 或者没有AC，都请标上每个题目大致花费时间。

3）提交时候先提交pdf文件，再把md或者doc文件上传到右侧“作业评论”。Canvas需要有同学清晰头像、提交文件有pdf、"作业评论"区有上传的md或者doc附件。

4）如果不能在截止前提交作业，请写明原因。



## 1. 题目

### 04148: 生理周期

brute force, http://cs101.openjudge.cn/practice/04148

思路：



代码：

```python
s = []
while True:
    a, b, c, d = map(int, input().split())
    if a == b == c == d == -1:
        break
    else:
        s.append((a, b, c, d))
for index, x in enumerate(s):
    a, b, c, d = x
    if a == b == c:
        print(f'Case {index+1}: the next triple peak occurs in {21252-d+a} days.')
    else:
        while True:
            k = min([a, b, c])
            if a == b == c:
                print(f'Case {index+1}: the next triple peak occurs in {a-d} days.')
                break
            elif c == k:
                c += 33
            elif b == k:
                b += 28
            elif a == k:
                a += 23

```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![](https://github.com/Xingyu-Xiao/My-Picbed/raw/main/%E5%B1%8F%E5%B9%95%E6%88%AA%E5%9B%BE%202024-10-22%20192004.png)



### 18211: 军备竞赛

greedy, two pointers, http://cs101.openjudge.cn/practice/18211

思路：



代码：

```python
def f(p, s):
    s.sort()
    i = 0
    j = len(s)-1
    out = 0
    while i <= j:
        if p >= s[i]:
            out += 1
            p -= s[i]
            i += 1
        else:
            if j-i < 2:
                break
            else:
                if out > 0:
                    p += (s[j]-s[i])
                    i += 1
                    j -= 1
                else:
                    break
    return out


P = int(input())
S = list(map(int, input().split()))
print(f(P, S))

```



代码运行截图 ==（至少包含有"Accepted"）==

![](https://github.com/Xingyu-Xiao/My-Picbed/raw/main/%E5%B1%8F%E5%B9%95%E6%88%AA%E5%9B%BE%202024-10-22%20192306.png)



### 21554: 排队做实验

greedy, http://cs101.openjudge.cn/practice/21554

思路：



代码：

```python
n = int(input())
s = list(map(int, input().split()))
ss = list(zip(s, [i for i in range(1, n+1)]))
ss.sort()
output = [x[1] for x in ss]
print(*output)
out = 0
q = []
for x in ss[:n-1]:
    out = out + x[0]
    q.append(out)
print(f'{(sum(q)/n):.2f}')
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![](https://github.com/Xingyu-Xiao/My-Picbed/raw/main/%E5%B1%8F%E5%B9%95%E6%88%AA%E5%9B%BE%202024-10-22%20194011.png)



### 01008: Maya Calendar

implementation, http://cs101.openjudge.cn/practice/01008/

思路：



代码：

```python
i = int(input())
print(i)
months = ['pop', 'no', 'zip', 'zotz', 'tzec', 'xul', 'yoxkin', 'mol', 'chen', 'yax', 'zac', 'ceh', 'mac',
          'kankin', 'muan', 'pax', 'koyab', 'cumhu']
mons = ['imix', 'ik', 'akbal', 'kan', 'chicchan', 'cimi', 'manik', 'lamat', 'muluk', 'ok', 'chuen',
        'eb', 'ben', 'ix', 'mem', 'cib', 'caban', 'eznab', 'canac', 'ahau']
for _ in range(i):
    day, mon, year = input().split()
    d = int(day.strip('.'))
    year = int(year)
    if mon != 'uayet':
        n = d + months.index(mon)*20 + year*365 + 1
    else:
        n = d + year*365 + 361
    m = n % 20 - 1
    k = (n-1) % 13 + 1
    y = (n-1) // 260
    print(k, mons[m], y)
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![](https://github.com/Xingyu-Xiao/My-Picbed/raw/main/%E5%B1%8F%E5%B9%95%E6%88%AA%E5%9B%BE%202024-10-22%20192405.png)



### 545C. Woodcutters

dp, greedy, 1500, https://codeforces.com/problemset/problem/545/C

思路：



代码：

```python
n = int(input())
a = [tuple(map(int, input().split())) for _ in range(n)]
if n > 1:
    out = 2
    last = a[0][0]
    for i in range(1, n-1):
        x, h = a[i]
        if x-h > last:
            out += 1
            last = x
        elif x+h < a[i+1][0]:
            out += 1
            last = x+h
        else:
            last = x
    print(out)
else:
    print(1)
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![](https://github.com/Xingyu-Xiao/My-Picbed/raw/main/%E5%B1%8F%E5%B9%95%E6%88%AA%E5%9B%BE%202024-10-22%20214240.png)



### 01328: Radar Installation

greedy, http://cs101.openjudge.cn/practice/01328/

思路：



代码：

```python
import math
i = 0
while True:
    try:
        n, d = map(int, input().split())
    except ValueError:
        continue
    if (n, d) == (0, 0):
        break
    a = [tuple(map(int, input().split())) for _ in range(n)]
    i += 1
    if any(y[1] for y in a if y[1] > d):
        print(f'Case {i}: -1')
    else:
        s = [(x-math.sqrt(d**2-y**2), x+math.sqrt(d**2-y**2)) for x, y in a]
        s.sort(key=lambda x: x[1])
        last = s[0][1]
        out = 1
        for x in s[1:]:
            if x[0] > last:
                out += 1
                last = x[1]
        print(f'Case {i}: {out}')
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![](https://github.com/Xingyu-Xiao/My-Picbed/raw/main/%E5%B1%8F%E5%B9%95%E6%88%AA%E5%9B%BE%202024-10-22%20224320.png)



## 2. 学习总结和收获

<mark>如果作业题目简单，有否额外练习题目，比如：OJ“计概2024fall每日选做”、CF、LeetCode、洛谷等网站题目。</mark>

有时候虽然思路基本上对了，但是会犯一些很愚蠢的错误又一直发现不了导致一个题目做好久，比如说在写判断语句的时候很容易漏情况，不知道有没有什么方法来规避或者帮助自己找到错误（GPT在纠错方面的能力很差，当他的代码和我的思路不一样是也很难根据我的思路写出正确的代码）



