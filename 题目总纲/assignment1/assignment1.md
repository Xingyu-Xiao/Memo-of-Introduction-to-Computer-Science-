# Assignment #1: 自主学习

Updated 0110 GMT+8 Sep 10, 2024

2024 fall, Complied by ==肖行宇 物理学院==



**说明：**

1）请把每个题目解题思路（可选），源码Python, 或者C++（已经在Codeforces/Openjudge上AC），截图（包含Accepted），填写到下面作业模版中（推荐使用 typora https://typoraio.cn ，或者用word）。AC 或者没有AC，都请标上每个题目大致花费时间。

3）课程网站是Canvas平台, https://pku.instructure.com, 学校通知9月19日导入选课名单后启用。**作业写好后，保留在自己手中，待9月20日提交。**

提交时候先提交pdf文件，再把md或者doc文件上传到右侧“作业评论”。Canvas需要有同学清晰头像、提交文件有pdf、"作业评论"区有上传的md或者doc附件。

4）如果不能在截止前提交作业，请写明原因。



## 1. 题目

### 02733: 判断闰年

http://cs101.openjudge.cn/practice/02733/



思路：



##### 代码

```python
a = int(input())
if a % 4 == 0:
    if a % 100 == 0:
        if a % 400 == 0:
            if a % 3200 != 0:
                print("Y")
        else:
            print("N")
    else:
        print("Y")
else:
    print("N")


```



代码运行截图 ====

![屏幕截图 2024-09-21 103225](https://raw.githubsercontent.com/Xingyu-Xiao/My-Picbed/main/undefined%E5%B1%8F%E5%B9%95%E6%88%AA%E5%9B%BE%202024-09-21%20103225.png)



### 02750: 鸡兔同笼

http://cs101.openjudge.cn/practice/02750/



思路：



##### 代码

```python
a = int(input())
if a % 2 == 0 and a > 0:
    if a % 4 == 0:
        print(a//4, a//2)
    else:
        print(a//4+1, a//2)
else:
    print(0, 0)


```



代码运行截图 ==（至少包含有"Accepted"）==

![](https://raw.githubsercontent.com/Xingyu-Xiao/My-Picbed/main/undefined%E5%B1%8F%E5%B9%95%E6%88%AA%E5%9B%BE%202024-09-24%20172653.png)



### 50A. Domino piling

greedy, math, 800, http://codeforces.com/problemset/problem/50/A



思路：



##### 代码

```python
a, b = input().split()
M = int(a)
N = int(b)
if M % 2 == 0 or N % 2 == 0:
    print(int(M*N/2))
else:
    x = N//2
    y = (M-1)*N/2
    print(int(x+y))


```



代码运行截图 ==（AC代码截图，至少包含有"Accepted"）==

![](https://raw.githubsercontent.com/Xingyu-Xiao/My-Picbed/main/undefined%E5%B1%8F%E5%B9%95%E6%88%AA%E5%9B%BE%202024-09-24%20173021.png)



### 1A. Theatre Square

math, 1000, https://codeforces.com/problemset/problem/1/A



思路：



##### 代码

```python
x, y, z = input().split()
x, y, z = int(x), int(y), int(z)
if x % z == 0:
    a = x//z
    if y % z == 0:
        b = y//z
        print(a * b)
    else:
        b = y // z + 1
        print(a * b)
if x % z != 0:
    a = x // z+1
    if y % z != 0:
        b = y//z+1
        print(a * b)
    else:
        b = y // z
        print(a * b)


```



代码运行截图 ==（AC代码截图，至少包含有"Accepted"）==

![](https://raw.githubsercontent.com/Xingyu-Xiao/My-Picbed/main/undefined%E5%B1%8F%E5%B9%95%E6%88%AA%E5%9B%BE%202024-09-24%20173157.png)



### 112A. Petya and Strings

implementation, strings, 1000, http://codeforces.com/problemset/problem/112/A



思路：



##### 代码

```python
a = input()
b = input()
a = a.lower()
b = b.lower()
la = list(a)
lb = list(b)
if la == lb:
    print(0)
else:
    for i in range(len(la)):
        if la[0] == lb[0]:
            del lb[0]
            del la[0]
    lab = [la[0], lb[0]]
    lab_sort = sorted(lab)
    if lab == lab_sort:
        print(-1)
    else:
        print(1)


```



代码运行截图 ==（AC代码截图，至少包含有"Accepted"）==

![alt](C:\Users\XXY13\AppData\Roaming\Typora\typora-user-images\image-20240924173341733.png)



### 231A. Team

bruteforce, greedy, 800, http://codeforces.com/problemset/problem/231/A



思路：



##### 代码

```python
a = int(input())


def f():
    data = []
    y = 0
    for i in range(a):
        s = input()
        data.append(s)
    return data


b = f()
i = 0
for line in b:
    ss = list(line.split())
    for j in range(len(ss)):
        ss[j] = int(ss[j])
    value = ss[0] + ss[1] + ss[2]
    if int(value) > 1:
        i += 1
print(i)


```



代码运行截图 ==（AC代码截图，至少包含有"Accepted"）==

![image-20240924173506117](C:\Users\XXY13\AppData\Roaming\Typora\typora-user-images\image-20240924173506117.png)



## 2. 学习总结和收获

==如果作业题目简单，有否额外练习题目，比如：OJ“计概2024fall每日选做”、CF、LeetCode、洛谷等网站题目。==

开始做题有一些困难，到现在已经跟上每日选做的进度并可以较为轻松地完成，感觉用GPT学习确实比较方便快速。



