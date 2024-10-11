# Assign #3: Oct Mock Exam暨选做题目满百

Updated 1537 GMT+8 Oct 10, 2024

2024 fall, Complied by Hongfei Yan==（肖行宇 物理学院）==



**说明：**

1）Oct⽉考： AC6==（5）== 。考试题⽬都在“题库（包括计概、数算题目）”⾥⾯，按照数字题号能找到，可以重新提交。作业中提交⾃⼰最满意版本的代码和截图。

2）请把每个题目解题思路（可选），源码Python, 或者C++/C（已经在Codeforces/Openjudge上AC），截图（包含Accepted, 学号），填写到下面作业模版中（推荐使用 typora https://typoraio.cn ，或者用word）。AC 或者没有AC，都请标上每个题目大致花费时间。

3）提交时候先提交pdf文件，再把md或者doc文件上传到右侧“作业评论”。Canvas需要有同学清晰头像、提交文件有pdf、作业评论有md或者doc。

4）如果不能在截止前提交作业，请写明原因。



## 1. 题目

### E28674:《黑神话：悟空》之加密

http://cs101.openjudge.cn/practice/28674/



思路：首先各建立一个大小写的字母列表，对输入的字母，判断其大小写及字母序列，原序列加上k对26取模即为新序列，从列表读取并输出即可。



代码

```python
n = int(input())
s = list(input())
ss = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
      'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
SS = [x.upper() for x in ss]
for index, x in enumerate(s):
    if x in ss:
        k = ss.index(x)
        kk = (k-n) % 26
        s[index] = ss[kk]
    else:
        i = SS.index(x)
        s[index] = SS[(i-n) % 26]
print(''.join(map(str, s)))


```



代码运行截图 ==（至少包含有"Accepted"）==

![](https://github.com/Xingyu-Xiao/My-Picbed/raw/main/%E5%B1%8F%E5%B9%95%E6%88%AA%E5%9B%BE%202024-10-10%20190759.png)



### E28691: 字符串中的整数求和

http://cs101.openjudge.cn/practice/28691/



思路：先建立一个数字列表，对于输入，判断其是否为数字（即在列表中），如果是，依次存进一空列表中，输出完成后，再换成字符串并转成整数存入另一列表，对列表求和即可。



代码

```python
s = list(input().split())
d = {'1', '2', '3', '4', '5', '6', '7', '8', '9', '0'}
a = []
for x in s:
    b = []
    for y in x:
        if y in d:
            b.append(y)
    a.append(int(''.join(b)))
print(sum(a))

```



代码运行截图 ==（至少包含有"Accepted"）==

![](https://github.com/Xingyu-Xiao/My-Picbed/raw/main/%E5%B1%8F%E5%B9%95%E6%88%AA%E5%9B%BE%202024-10-10%20204248.png)



### M28664: 验证身份证号

http://cs101.openjudge.cn/practice/28664/



思路：



代码

```python
s = [1, 0, 10, 9, 8, 7, 6, 5, 4, 3, 2]
n = int(input())
a = [list(input()) for _ in range(n)]
for x in a:
    if x[17] == 'X':
        x[17] = 10
    x = list(map(int, x))
    k = (7*x[0] + 9*x[1] + 10*x[2] +5*x[3] +8*x[4]+4*x[5] +2*x[6]+x[7]+6*x[8]+3*x[9]+7*x[10]+9*x[11]
         +10*x[12]+5*x[13]+8*x[14]+4*x[15]+2*x[16])
    k = k % 11
    if s[k] == x[17]:
        print('YES')
    else:
        print('NO')

```



代码运行截图 ==（AC代码截图，至少包含有"Accepted"）==

![](https://github.com/Xingyu-Xiao/My-Picbed/raw/main/%E5%B1%8F%E5%B9%95%E6%88%AA%E5%9B%BE%202024-10-10%20204455.png)



### M28678: 角谷猜想

http://cs101.openjudge.cn/practice/28678/



思路：



代码

```python


```



代码运行截图 ==（AC代码截图，至少包含有"Accepted"）==





### M28700: 罗马数字与整数的转换

http://cs101.openjudge.cn/practice/28700/



思路：



##### 代码

```python
# 

```



代码运行截图 ==（AC代码截图，至少包含有"Accepted"）==





### *T25353: 排队 （选做）

http://cs101.openjudge.cn/practice/25353/



思路：



代码

```python


```



代码运行截图 ==（AC代码截图，至少包含有"Accepted"）==





## 2. 学习总结和收获

==如果作业题目简单，有否额外练习题目，比如：OJ“计概2024fall每日选做”、CF、LeetCode、洛谷等网站题目。==











