python 从字符串中提取数字

```
my_str = '123and456'

number = filter(str.isdigit,  my_str )

# number = 123456
```

### 使用正则表达式：

```
>>> import re

>>> re.findall(r'\d+', 'hello 42 I\'m a 32 string 30')

['42', '32', '30']
```

### 这也将匹配 42 bla42bla。如果您只想要按字边界（空格，句号，逗号）分隔的数字，则可以使用\ b：

```
>>> re.findall(r'\b\d+\b', 'he33llo 42 I\'m a 32 string 30')

['42', '32', '30']
```

最终得到一个数字列表而不是字符串列表：

```
>>> [int(s) for s in re.findall(r'\b\d+\b', 'he33llo 42 I\'m a 32 string 30')]

[42, 32, 30]
```

### 示例:

python str.isdigit() 有浮点数的判断

```
str.isdigit() 是个很好的工具，用来判断字符串中是否全为数字。而浮点数因为有 "." ，所以会返还FALSE。

参考示例：

# 提示用户输入圆的半径，计算出该圆的周长和面积。要求如下：
# 圆周率 π 值取 3.1415926
# 如果输入的是负数和零，提示半径不能负数或者零
# 计算机的结果保留两位小数

if __name__ == "__main__":
    PI = 3.1415926
    radius = input("请输入圆的半径：")
    print(radius)
    print(radius.isdigit())
    if radius.isdigit():
        radius = float(radius)
        # 计算元的周长和面积
        circle_perimeter = 2 * PI * radius
        circle_area = PI * radius * radius
        print("圆的周长：%.2f \n圆的面积：%.2f" % (circle_perimeter, circle_area))

    else:
        print("半径不能负数或者零")
以上在输入半径：12.3 就会报错 。

此时需要replace() 方法语法：

str.replace(old, new[, max])

参数

old -- 将被替换的子字符串。
new -- 新字符串，用于替换old子字符串。
max -- 可选字符串, 替换不超过 max 次

if radius.replace(".", "").isdigit():   # 替换为空即可。

```

### 闰年 判断的两种方式'

```
首先明确  什么是闰年？

1、能被4整除，但不能被100整除；

2、能被400整除；

 

方案一：

while True:
    year = input("请输入要判断的年份（例如：2000）：")
    if  year.isdigit():
        year = int(year)
        result = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
        if result:
            s = "是"
        else:
            s = "不是"
        print("{0}年{1}闰年".format(year, s))
    else:
        print("请输入年份！")
 

方案二：

while True:
    year = input("请输入您要判断的年份（例如：2000）：")
    if  year.isdigit():
        year = int(year)
        result = (year/400 == int(year/400))or((year/4 == int(year/4)) and (year/100 != int(year/100)))
        if result:
            s = "是"
        else:
            s = "不是"
        print("{0}年{1}闰年!".format(year, s))
    else:
        print("请输入年份！")
 

方案三：

while True:
    year = input("请输入您要判断的年份（例如：2000）：")
    if  year.isdigit():
        yea = int(year)
        if (yea/400 == int(yea/400))or((yea/4 == int(yea/4)) and (yea/100 != int(yea/100))):
            print(year+"是闰年!")
        else:
            print(year+"不是闰年!")
    else:
        print("请输入年份！")

```

### 字典的应用

```
import random
from collections import defaultdict

nums = []
for count in range(50):
    nums.append(random.randint(1,100))
sort_nums_dict=defaultdict(list)
for num in nums:
    if num>66:
        sort_nums_dict['大于66的元素'].append(num)
    else:
        sort_nums_dict['小于66的元素'].append(num)
print(sort_nums_dict)

```

###

```
import re
s = re.findall(r'\d+', 'hello 42 I\'m a 32 string 30')
list_ = []
sum_=0
for i in s:
    s1=int(i)
    list_.append(s1)
print(list_)
for i in list_:
    sum_+=i
print(sum_)

```

运行结果：

```
[42, 32, 30]
104
```
