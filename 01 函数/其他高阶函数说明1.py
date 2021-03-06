'''
示例：筛选质数

质数定义为在大于 1 的自然数中，除了 1 和它本身以外不再有其他因数。

因数，或称为约数，数学名词。定义：整数 a 除以整数 b(b≠0) 的商正好是整数而没有余数，我们就说 b 是 a 的因数。0 不是 0 的因数。

计算质数的一个方法是埃氏筛法，它的算法理解起来非常简单：

首先，列出从 2 开始的所有自然数，构造一个序列：

2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, ...

取序列的第一个数 2，它一定是素数，然后用 2 把序列的 2 的倍数筛掉：

3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, ...

取新序列的第一个数 3，它一定是素数，然后用 3 把序列的 3 的倍数筛掉：

5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, ...

取新序列的第一个数 5，然后用 5 把序列的 5 的倍数筛掉：

7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, ...

不断筛下去，就可以得到所有的素数。

# 先构造一个从 3 开始的奇数序列
'''


def _odd_iter():
    n = 1

    while True:

        n = n + 2

    yield n  # yield 返回的是一个生成器，所包含的序列将是无限的

# 定义一个筛选函数，


def _not_divisible(n):

    return lambda x: x % n > 0  # 这里将 lambda 匿名函数返回

# 定义一个生成器函数


def primes():

    yield 2  # 事先在生成器里返回了 2


it = _odd_iter()  # 初始序列，这里都是奇数，返回的是一个生成器

while True:
    n = next(it)  # 返回序列的第一个数，之后返回下一个
    yield n

it = filter(_not_divisible(n), it)  # 构造新序列，每次将所有奇数作用于筛选函数返回的函数上

# 打印 100 以内的素数:

l = []

for n in primes():
    if n < 100:
        l.append(n)
    else:
        break

print(l)

'''
[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41,
    43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]

yield 是一个类似 return 的关键字，只是这个函数返回的是个生成器

当你调用这个函数的时候，函数内部的代码并不立马执行 ，这个函数只是返回一个生成器对象

当你使用 for 进行迭代的时候，函数中的代码才会执行

sorted() 函数

sorted() 函数是 python 中内置的函数，可以对 list 进行排序

示例：
'''

'''
l = sorted([1, 4, 5, 2, 3])

print(l)

[1, 2, 3, 4, 5]

此外，sorted() 函数也是一个高阶函数，它还可以接收一个 key 函数来实现自定义的排序

示例：按绝对值大小排序

# 按大小排序

l = sorted([1, -5, 3, -2, -4])

print(l)

# 按绝对值排序

l = sorted([1, -5, 3, -2, -4], key=abs)

print(l)

[-5, -4, -2, 1, 3]

[1, -2, 3, -4, -5]

key 指定的函数将作用于 list 的每一个元素上，并根据 key 函数返回的结果进行排序

sorted() 也可以对字符串进行排序，示例：

l_str = sorted(['hello', 'my', 'name', 'is', 'Jack'])

print(l_str)

['Jack', 'hello', 'is', 'my', 'name']

默认情况下，对字符串排序，是按照 ASCII 的大小比较的，由于 'J' < 'a'，结果，大写字母 J 会排在小写字母 h 的前面

如果纯粹的想按字母进行排序，而不分大小写，则可以将所有的字母都转换成小写，再来进行排序，示例如下：

l_str = sorted(['hello', 'my', 'name', 'is', 'Jack'], key=str.lower)

print(l_str)

['hello', 'is', 'Jack', 'my', 'name']

还可以反向排序，需要第三个参数 reverse = True，示例如下：

l_str = sorted(['hello', 'my', 'name', 'is', 'Jack'],
               key=str.lower, reverse=True)

print(l_str)

['name', 'my', 'Jack', 'is', 'hello']
'''
