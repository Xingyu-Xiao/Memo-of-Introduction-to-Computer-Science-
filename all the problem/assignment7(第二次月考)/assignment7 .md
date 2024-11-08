# Assignment #7: Nov Mock Exam立冬

Updated 1646 GMT+8 Nov 7, 2024

2024 fall, Complied by <mark>肖行宇   物理学院</mark>



**说明：**

1）⽉考： AC6<mark>（6）</mark> 。考试题⽬都在“题库（包括计概、数算题目）”⾥⾯，按照数字题号能找到，可以重新提交。作业中提交⾃⼰最满意版本的代码和截图。

2）请把每个题目解题思路（可选），源码Python, 或者C++（已经在Codeforces/Openjudge上AC），截图（包含Accepted），填写到下面作业模版中（推荐使用 typora https://typoraio.cn ，或者用word）。AC 或者没有AC，都请标上每个题目大致花费时间。

3）提交时候先提交pdf文件，再把md或者doc文件上传到右侧“作业评论”。Canvas需要有同学清晰头像、提交文件有pdf、"作业评论"区有上传的md或者doc附件。

4）如果不能在截止前提交作业，请写明原因。



## 1. 题目

### E07618: 病人排队

sorttings, http://cs101.openjudge.cn/practice/07618/

思路：



代码：

```python
n = int(input())
s = [[_] + list(input().split()) for _ in range(n)]
s_60 = [x for x in s if int(x[2]) >= 60]
ss = [x for x in s if int(x[2]) < 60]
s_60.sort(key=lambda x: (-int(x[2]), x[0]))
ans = s_60 + ss
for y in ans:
    print(y[1])
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![](https://github.com/Xingyu-Xiao/My-Picbed/raw/main/%E5%B1%8F%E5%B9%95%E6%88%AA%E5%9B%BE%202024-11-07%20170803.png)



### E23555: 节省存储的矩阵乘法

implementation, matrices, http://cs101.openjudge.cn/practice/23555/

思路：



代码：

```python
n, m_1, m_2 = map(int, input().split())
s_1 = [[0 for _ in range(n)] for _ in range(n)]
s_2 = [[0 for _ in range(n)] for _ in range(n)]
for _ in range(m_1):
    i, j, k = map(int, input().split())
    s_1[i][j] = k
for _ in range(m_2):
    i, j, k = map(int, input().split())
    s_2[i][j] = k
ans = [[0 for _ in range(n)] for _ in range(n)]
for i in range(n):
    for j in range(n):
        ans[i][j] = sum(s_1[i][k]*s_2[k][j] for k in range(n))
        if ans[i][j] != 0:
            print(i, j, ans[i][j])
```



代码运行截图 ==（至少包含有"Accepted"）==

![](https://github.com/Xingyu-Xiao/My-Picbed/raw/main/%E5%B1%8F%E5%B9%95%E6%88%AA%E5%9B%BE%202024-11-07%20171023.png)



### M18182: 打怪兽 

implementation/sortings/data structures, http://cs101.openjudge.cn/practice/18182/

思路：



代码：

```python
def solve(s, n, m, b):
    count = 1
    b -= s[0][1]
    if b <= 0:
        return s[0][0]
    for i in range(1, n):
        if s[i][0] == s[i-1][0]:
            if count == m:
                continue
            else:
                b -= s[i][1]
                count += 1
        else:
            b -= s[i][1]
            count = 1
        if b <= 0:
            return s[i][0]
    return 'alive'


n_case = int(input())
for _ in range(n_case):
    n, m, b = map(int, input().split())
    s = [tuple(map(int, input().split())) for _ in range(n)]
    s.sort(key=lambda x: (x[0], -x[1]))
    print(solve(s, n, m, b))
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![](https://github.com/Xingyu-Xiao/My-Picbed/raw/main/%E5%B1%8F%E5%B9%95%E6%88%AA%E5%9B%BE%202024-11-07%20171038.png)



### M28780: 零钱兑换3

dp, http://cs101.openjudge.cn/practice/28780/

思路：



代码：

```python
n, m = map(int, input().split())
s = list(map(int, input().split()))
dp = [m+1]*(m+1)
dp[0] = 0
for i in range(1, m+1):
    add = []
    for x in s:
        add_x = dp[i-x] + 1 if (i-x >= 0 and dp[i-x] < m+1) else m+1
        add.append(add_x)
    dp[i] = min(add)
if dp[-1] != m+1:
    print(dp[-1])
else:
    print(-1)
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![](https://github.com/Xingyu-Xiao/My-Picbed/raw/main/%E5%B1%8F%E5%B9%95%E6%88%AA%E5%9B%BE%202024-11-07%20171058.png)



### T12757: 阿尔法星人翻译官

implementation, http://cs101.openjudge.cn/practice/12757

思路：



代码：

```python
word = {'zero':0, 'one':1, 'two':2, 'three':3, 'four':4, 'five':5, 'six':6,
        'seven':7, 'eight':8, 'nine':9, 'ten':10, 'eleven':11, 'twelve':12, 'thirteen':13,
        'fourteen':14, 'fifteen':15, 'sixteen':16, 'seventeen':17, 'eighteen':18, 'nineteen':19,
        'twenty':20, 'thirty':30, 'forty':40, 'fifty':50, 'sixty':60, 'seventy':70,
        'eighty':80, 'ninety':90}


def f(a):
    return sum(word[x] for x in a)


def hundred(a):
    if 'hundred' in a:
        index_h = a.index('hundred')
        return sum(word[x] for x in a[:index_h])*100 + f(a[index_h+1:])
    else:
        return f(a)


def thousand(a):
    if 'thousand' in a:
        index_t = a.index('thousand')
        return hundred(a[:index_t])*1000 + hundred(a[index_t+1:])
    else:
        return hundred(a)


def million(a):
    if 'million' in a:
        index_m = a.index('million')
        return thousand(a[:index_m])*1000000 + thousand(a[index_m+1:])
    else:
        return thousand(a)


ans = []
s = list(input().split())
if s[0] == 'negative':
    ans.append('-')
    s = s[1:]
ans.append(str(million(s)))
print(''.join(ans))
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![](https://github.com/Xingyu-Xiao/My-Picbed/raw/main/%E5%B1%8F%E5%B9%95%E6%88%AA%E5%9B%BE%202024-11-07%20171119.png)



### T16528: 充实的寒假生活

greedy/dp, cs10117 Final Exam, http://cs101.openjudge.cn/practice/16528/

思路：



代码：

```python
n = int(input())
s = [tuple(map(int, input().split())) for _ in range(n)]
s.sort(key=lambda x: (x[1], -x[0]))
ans = 1
last = s[0][1]
for x in s[1:]:
    if x[0] > last:
        ans += 1
        last = x[1]
    else:
        continue
print(ans)
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![](https://github.com/Xingyu-Xiao/My-Picbed/raw/main/%E5%B1%8F%E5%B9%95%E6%88%AA%E5%9B%BE%202024-11-07%20171143.png)



## 2. 学习总结和收获

<mark>如果作业题目简单，有否额外练习题目，比如：OJ“计概2024fall每日选做”、CF、LeetCode、洛谷等网站题目。</mark>

这次的月考做的很顺利，虽然涉及到了dp和贪心但都是比较基础的题目，但是机房的电脑用起来还是很不顺手:dizzy_face:

另外之前因为期中考试每日选做停留了一段时间，现在正在追赶。

