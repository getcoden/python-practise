# 创建一个函数，输出给定数字与 17 的差值，如果数字大于 17，则输出的差值乘以 2
'''
def difference(x):
    if x > 17:
        return (x - 17) * 2
    else:
        return x - 17


print(difference(12))
print(difference(20))
'''
# 创建一个函数，给定一个字符串，是否以 Is 开头，是的话返回字符串，否则在原字符串前面增加 Is


# def func(str):
#     if str[:2] == 'ls':
#         return str
#     else:
#         return 'ls' + str


# print(func('a'))

# 创建一个函数，输入一个数字，判断是奇数还是偶数

# def isodd():
#     n = int(input('输入一个数字:'))
#     mod = n % 2
#     if mod > 0:
#         return 'this is an even number'
#     else:
#         return 'this is a odd number'


# print(isodd())

# 创建一个函数，给定三个数字，如果三个数字相等，则输出三个数字和的三倍
def func2(x, y, z):
    sum = x + y + z
    if x == y == z:
        sum = 3 * sum
        return sum
    else:
        return sum


print(func2(1, 2, 3))
print(func2(2, 2, 2))


# Python3 的主要特征
# 
# 封装：封装指的是把一堆数据属性与方法数据放在一个容器中，这个容器就是对象。让对象可以通过 "." 来调用对象中的数据属性与方法属性。
# 
# 继承：继承指的是子类可以继承父类的数据属性与方法属性，并可以对其进行修改或使用。 多态：在 python 中的多态指的是让多种类若具备类似的数据属性与方法属性，都统一好命名规范，这样可以提高开发者的代码统一性，使得调用者更方便去理解。


