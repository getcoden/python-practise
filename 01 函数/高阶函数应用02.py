import random
from functools import reduce

# 定义普通函数，自动生成列表


def getList():
    hList = list(range(5))
    return [key * random.randint(0, 3) for key in hList]  # 生成随机数

# 定义普通函数，求不同列表中最大并集


def getMaxSet(listA, listB):
    setA = set(listA)  # 转为set
    setB = set(listB)
    setAll = setA | setB  # 求并集
    return list(setAll)  # 转为list

# 定义高阶函数


def highFunction(listA, listB, getMaxSet):
    return getMaxSet(listA, listB)


# 获取两个集合
listA = getList()
print("集合A:{}".format(listA))
listB = getList()
print("集合B:{}".format(listB))

# 获取两个集合的并集
listC = getMaxSet(listA, listB)
print("集合A和集合B的并集:{}".format(listC))

# 调用高阶函数
values = highFunction(listA, listB, getMaxSet)
print("调用高阶函数获取集合A和集合B的并集:{}".format(values))
