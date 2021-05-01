import calendar
from functools import reduce


def func_square(num):
    return num ** 2


num_list = map(func_square, [1, 2, 3, 4, 5, 6, 7, 8, 9])
print(list(num_list))

print(list(map(str, [1, 2, 3, 4, 5, 6, 7, 8, 9])))

'''
reduce () 函数

reduce () 函数将一个函数作用在一个序列上，这个函数必须接收两个参数，reduce () 函数会继续和序列的下一个元素做累积运算
'''


def add(x, y):
    return x + y


result = reduce(add, [1, 2, 3, 4, 5])
print(result)

# 序列 [1, 2, 3, 4, 5] 的每一个元素作用到 add () 方法上，将该函数得到的结果再与下一个元素传入 add () 方法中，直到结束，得到的结果就是 1+2+3+4+5=15

'''
示例：如何将序列 [1, 2, 3, 4, 5] 转换成数字 12345

# 从 functolls 模块中导入 reduce 函数

from functools import reduce

# 定义一个转换函数

'''


def fn(x, y):
    return x * 10 + y


re = reduce(fn, [1, 2, 3, 4, 5])
print(re)


def char_num(x):
    return int(x)


r = reduce(fn, map(char_num, '12345'))
print(r)


'''
filter () 函数

filter () 函数接收一个函数和一个序列作为参数，并将序列中的每一个元素都作用到传入函数上，根据该函数返回的布尔值，来决定当前元素是否保留

示例：筛选一个序列，保留奇数

'''
# 奇数筛选函数


def is_odd(x):
    return x % 2 == 1


# 调用filter()函数
result1 = filter(is_odd, [1, 2, 3, 4, 5])
print(list(result1))

'''
示例：删除掉序列中的空字符串
'''
# 筛选空字符串


def empty_str(x):
    return x.strip() != ''


# 调用filter()函数
result2 = filter(empty_str, ['', '2', 'a', ''])
print(list(result2))


# 需求：将列表中的偶数筛选出来。

list1 = [1, 2, 3, 4, 5, 6, 7, 8]

# 筛选条件


def func(num):

    # 保留偶数元素
    if num % 2 == 0:

        return True

# 剔除奇数元素

    return False


list2 = filter(func, list1)

print(list2)

print(list(list2))

print(list1)

'''
注意：使用 filter() 这个高阶函数，关键在正确实现一个 “筛选” 函数，filter() 函数返回的是一个 Iterator，也就是一个惰性序列，所以要强迫 filter 完成计算结果，需要使用 list() 函数获取所有的结果并且返回 list.

练习

需求；将爱好为 “无” 的数据剔除掉
'''
data = [["姓名", "年龄", "爱好"], ["tom", 25, "无"], ["hanmeimei", 26, "金钱"]]

data = [["姓名", "年龄", "爱好"], ["tom", 25, "无"], ["hanmeimei", 26, "金钱"]]


def filterWu(list1):
    for i in list1:
        if i == "无":
            return False
    return True


dataFilter = list(filter(filterWu, data))

print(dataFilter)

# 练习 2，需求：打印 2000 到 2020 之内的闰年[使用 filter 函数]

print(list(filter(calendar.isleap, range(2000, 2020))))
