
'''
自除数
自除数是指可以被它包含的每一位数除尽的数。也可以理解为，自除数对组成其本身的每一位数字进行取余结果都为 0。需要注意，自除数不允许包含 0 。
例如，128 是一个自除数，因为 128 % 1 == 0，128 % 2 == 0，128 % 8 == 0。


题目：现在，给定上边界和下边界数字，输出一个列表，列表的元素是边界（含边界）内所有的自除数。请尝试编程解决


筛选自除数
1、首先将这个数的每一个数字提取出来。
2、检查数字中是否存在 0，如果存在，则判定不是自除数。
3、使用原数对每一位数字进行除法运算，判定是否存在余数非零结果。
'''


# def yyds(left, right):
#     l = []
#     for num in range(left, right+1):
#         numStr = str(num)
#         numList = list(str(num))
#         res = True
#         for item in numList:
#             itemNum = int(item)
#             if itemNum == 0:
#                 res = False
#                 break
#             if num % itemNum != 0:
#                 res = False
#         if res:
#             l.append(num)
#     return l


# print(yyds(1, 100))
