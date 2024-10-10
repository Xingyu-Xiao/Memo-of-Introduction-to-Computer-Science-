# Assignment #2: 语法练习

Updated 0126 GMT+8 Sep 24, 2024

2024 fall, Complied by ==肖行宇  物理学院==



**说明：**

1）请把每个题目解题思路（可选），源码Python, 或者C++（已经在Codeforces/Openjudge上AC），截图（包含Accepted），填写到下面作业模版中（推荐使用 typora https://typoraio.cn ，或者用word）。AC 或者没有AC，都请标上每个题目大致花费时间。

3）课程网站是Canvas平台, https://pku.instructure.com, 学校通知9月19日导入选课名单后启用。**作业写好后，保留在自己手中，待9月20日提交。**

提交时候先提交pdf文件，再把md或者doc文件上传到右侧“作业评论”。Canvas需要有同学清晰头像、提交文件有pdf、"作业评论"区有上传的md或者doc附件。

4）如果不能在截止前提交作业，请写明原因。



## 1. 题目

### 263A. Beautiful Matrix

https://codeforces.com/problemset/problem/263/A



思路：



##### 代码

```python
def matrix():
    s = []
    for j in range(5):
        s.append(input())
    return s


a = matrix()
for x in a:
    e = abs(a.index(x) - 2)
    p = list(x.split())
    if "1" in p:
        q = p.index("1")
        y = abs(q-2)
        print(e+y)

```



代码运行截图 ==（至少包含有"Accepted"）==

![image-20240924174809878](C:\Users\XXY13\AppData\Roaming\Typora\typora-user-images\image-20240924174809878.png)



### 1328A. Divisibility Problem

https://codeforces.com/problemset/problem/1328/A



思路：



##### 代码

```python
# 
a = int(input())


def f():
    s = []
    for j in range(a):
        s.append(input())
    return s


q = f()
for x in q:
    p = list(x.split())
    for i in range(len(p)):
        p[i] = int(p[i])
    h = p[0]//p[1]
    if p[0] % p[1] != 0:
        print((h+1)*p[1]-p[0])
    else:
        print(0)
```



代码运行截图 ==（至少包含有"Accepted"）==

![image-20240924174935262](C:\Users\XXY13\AppData\Roaming\Typora\typora-user-images\image-20240924174935262.png)



### 427A. Police Recruits

https://codeforces.com/problemset/problem/427/A



思路：



##### 代码

```python
# 
b = int(input())
a = list(map(int, input().split()))


def f(n, m):
    x = 0
    y = 0
    for o in m:
        if o < 0:
            if y > 0:
                y += o
            else:
                x -= o
        else:
            y += o
    return x


print(f(b, a))


```



代码运行截图 ==（AC代码截图，至少包含有"Accepted"）==

![image-20240924175024791](C:\Users\XXY13\AppData\Roaming\Typora\typora-user-images\image-20240924175024791.png)



### 02808: 校门外的树

http://cs101.openjudge.cn/practice/02808/



思路：



##### 代码

```python
# 
total, n = map(int, input().split())
qq = [True]*(total+1)
for i in range(n):
    q = list(map(int, input().split()))
    for j in range(q[0], q[1]+1):
        qq[j] = False
print(sum(qq))

```



代码运行截图 ==（AC代码截图，至少包含有"Accepted"）==

![image-20240924175145603](C:\Users\XXY13\AppData\Roaming\Typora\typora-user-images\image-20240924175145603.png)



### sy60: 水仙花数II

https://sunnywhy.com/sfbj/3/1/60



思路：



##### 代码

```python
# 
a, b = map(int, input().split())
s = []
p = True
for i in range(a, b+1):
    i_1, i_2, i_3 = map(int,[str(i)[0], str(i)[1], str(i)[2]])
    if i_1**3 + i_2**3 + i_3**3 == i:
        s.append(i)
        p = False
if not p:
    print(' '.join(map(str, s)))
else:
    print('NO')

```



代码运行截图 ==（AC代码截图，至少包含有"Accepted"）==

![image-20240924175301295](C:\Users\XXY13\AppData\Roaming\Typora\typora-user-images\image-20240924175301295.png)



### 01922: Ride to School

http://cs101.openjudge.cn/practice/01922/



思路：



##### 代码

```python
# 
import math
ss = []
while True:
    n = int(input())
    if n == 0:
        break
    else:
        s = []
        for i in range(n):
            a, b = map(int, input().split())
            s.append([a, b])
        ss.append(s)
for s in ss:
    time = [(4500*3.6/x[0]+x[1]) for x in s if x[1] >= 0]
    print(math.ceil(min(time)))
```



代码运行截图 ==（AC代码截图，至少包含有"Accepted"）==

![image-20240924212407905](C:\Users\XXY13\AppData\Roaming\Typora\typora-user-images\image-20240924212407905.png)



## 2. 学习总结和收获

==如果作业题目简单，有否额外练习题目，比如：OJ“计概2024fall每日选做”、CF、LeetCode、洛谷等网站题目。==

感觉最近几天的每日选做似乎有些简单了，可以稍微增加难度。



