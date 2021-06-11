
'''
lis = [56, 12, 1, 8, 354, 10, 100, 34, 56, 7, 23, 456, 234, -58]
def sortport():
    for i in range(len(lis) - 1):
        for j in range(len(lis) - 1 - i):
            if lis[j] > lis[j + 1]:
                lis[j], lis[j + 1] = lis[j + 1], lis[j]
    return lis


if __name__ == '__main__':
    sortport()
    print(lis)

'''

# 另一种写法

import random

# i_list = []
# for i in range(10):
#     i_list.append(random.randrange(1000))
# print('原始随机列表为:' + str(i_list))
# for i in range(1, len(i_list)):
#     for j in range(0, len(i_list) - 1):
#         if i_list[j] >= i_list[j + 1]:
#             i_list[j], i_list[j + 1] = i_list[j + 1], i_list[j]
#     print('第'+str(i)+'轮排序结果为:'+str(i_list))

# 从指定范围内，按指定基数递增的集合中 获取一个随机数。[start] 以及 [,step] 的缺省值为 1
print(random.randrange(10, 20, 2))  # 在列表[10，12，14，16，18]之间随机取一个数


'''
random.choice(sequence)
从序列中获取一个随机元素。参数 sequence 表示一个有序类型。这里要说明 一下：sequence 在 python 不是一种特定的类型，而是泛指一系列的类型。list, tuple, 字符串都属于 sequence。
'''
USER_AGENTS = [
    'Mozilla/5.0 (iPhone; CPU iPhone OS 14_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148',
    'Mozilla/5.0 (iPhone; CPU iPhone OS 14_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 SGInfo/750/1624/2 Sogousearch/Ios/7.8.8 NoHead',
    'Mozilla/5.0 (iPhone; CPU iPhone OS 9_3_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 Mobile/13E238 Safari/601.1',
]


def get_header():
    return {
        'User-Agent': random.choice(USER_AGENTS),
    }


print(get_header())
