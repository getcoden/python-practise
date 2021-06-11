# s1 = '\'hello,world!\''
# s2 = '\n\\hello,world!\\\n'
# print(s1, s2, end='')

# s3 = r'\'hello,world!\''
# s4 = r'\n\\hello,world!\\\n'
# print(s3, s4, end='')

# s5 = '\nhello'*3
# print(f'\n这是f5{s5}')

# s6 = 'world'
# s5 += s6
# print(s5)

# str2 = 'abc123456'
# print(str2[2])
# print(str2[2:5])

'''
# 通过循环用下标遍历列表元素
list1 = [1, 3, 5, 7, 100]
for index in range(len(list1)):
    print(list1[index])
# 通过for 循环遍历列表元素
for elem in list1:
    print(elem)
# 通过enumerate函数处理列表之后再遍历可以同时获得元素索引和值
for index, elem in enumerate(list1):
    print(index, elem)
'''

# 下面的代码演示了如何向列表中添加元素以及如何从列表中移除元素。

list1 = [1, 3, 5, 7, 100]
# list1.append(200)
# list1.insert(1, 400)
# print(list1)
list1.extend([1000, 2000])
list1 += [123, 456]
print(list1)

# 先通过成员运算判断元素是否在列表中，如果存在就删除该元素
# if 3 in list1:
#     list1.remove(3)
# if 1234 in list1:
#     list1.remove(1234)
# print(list1)

# print(list1)
# list1.pop(0)
# list1.pop(len(list1)-1)
# print(list1)

fruits = ['grape', 'apple', 'strawberry', 'waxberry']
fruits += ['pitaya', 'pear', 'mango']
# 列表切片
fruits2 = fruits[1:4]
print(fruits2)  # apple strawberry waxberry
fruits3 = fruits[:]
print(fruits3)
fruits4 = fruits[-3:-1]
print(fruits4)
fruits5 = fruits[::-1]
print(fruits5)
