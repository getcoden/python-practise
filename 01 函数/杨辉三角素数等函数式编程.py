# 杨辉三角形，由用户输入三角形层数，直到输入 q 退出程序

'''
def print_pyramid(level: int):
    for i in range(level):
        new_line_str = ''
        new_line_str += ' ' * (level - 1 - i)
        new_line_str += '*' * ((i+1) * 2 - 1)
        print(new_line_str)


# input_level = int()
# print_pyramid(input_level)


while True:
    input_level = input('Enter a number:(q is quite)')
    if input_level == 'q':
        break
    else:
        input_level = int(input_level)
        print_pyramid(input_level)

'''
# def yang(i, j):
#     if j == 0 or j == i:
#         return 1
#     else:
#         return yang(i-1, j)+yang(i-1, j-1)


# for i in range(0, 10):
#     print()
#     for n in range(0, 10-i):
#         print("", end="")  # 控制每一行前面的空格
#     for j in range(0, i):
#         print(yang(i, j), "", end="")


# 传统的杨辉三角形实现
'''
def pascal(row):
    result_list = [0] * (row * 2 + 1)

    for row_loc in range(row):
        base_loc = row - row_loc - 1
        if row_loc == 0:
            result_list[base_loc] = 1
        else:
            result_list[base_loc] = result_list[base_loc + 1]
            for line_loc in range(row_loc):
                now_loc = base_loc + (line_loc + 1) * 2
                result_list[now_loc] = result_list[now_loc - 1] + \
                    result_list[now_loc + 1]
                result_list[now_loc - 1] = 0

        print(str(result_list)
              .replace("]", ",").replace(" 0,", "  ").replace(",", "").replace("[0", "  ").replace("[", " "))


pascal(5)

'''

# 利用python列表迭代的实现
# 第二种：基于 python 的列表迭代的思路
# 这个实现利用 python 的列表处理特性来实现，代码比传统思路要简洁很多，也还算好懂。缺点是仍然不够简洁。
# 代码如下（来自于毛豆子，原文链接：http: // www.cnblogs.com/maodouzi/archive/2011/07/12/2104153.html）：
'''
def printLine(lineList, row):
    lineList = [str(tmpNum) for tmpNum in lineList]
    print("%s%s" % (" " * (row - len(lineList)), " ".join(lineList)))


def pascal(row):
    for i in range(row):
        if i < 2:
            yhList = [1] * (i + 1)
        else:
            yhList[1:-1] = [(tmpNum + yhList[j])
                            for j, tmpNum in enumerate(yhList[1:])]
        printLine(yhList, row)


pascal(10)
'''
'''
1、这种易理解
L1 = []
count = 0
for x in range(1, 100):
    n = 0
    for y in range(1, x + 1):
        if x % y == 0:
            n = n + 1
    if n == 2:
        count += 1
        L1.append(x)
print(L1)
print(count)
'''
# 2、计算 2-100 之间素数的个数，返回结果。格式化字符串，标准


# def primeNum(f):
#     def f1():
#         sum_pri = 0
#         for i in range(2, 101):
#             for j in range(2, i):
#                 if i % j == 0:
#                     break
#                 elif j == i - 1:
#                     sum_pri += 1
#         return f(sum_pri+1)
#     return f1


# @primeNum
# def f(p):
#     print("2-100之间共有{}个素数".format(p))


# f()


l = []
number = input('请输入数字以空格 隔开>>>:').split()
number = [int(x) for x in number]
for i in number:
    i = i**2
    l.append(i)
print(l)
