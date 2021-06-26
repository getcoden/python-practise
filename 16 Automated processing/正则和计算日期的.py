import random
import pandas as pd
import numpy as np
from datetime import datetime, date, time
# my_randoms = random.sample(range(100), 10)
# test = pd.DataFrame(my_randoms, columns=["x"])
# print(test)

# ranges = [(0, 19), (20, 39), (40, 69)]
# cnt = []
# for range in ranges:
#     tmp = ranges[(ranges['x'] > range[0]) & (range['x'] <= range[1])]
#     cnt.append(len(tmp))
# print(cnt)

# print(test.groupby(pd.cut(test['x'], np.arange(0, 100, 20))).count())


import re

# line01 = 'boooboaobcxby'


# def regtest_test(reg_str, line=line01):
#     test = re.match(reg_str, line)
#     if test:
#         print(test.group(1)+':'+test.group(2) +
#               '-'+test.group(3)+'-'+test.group(4))
#     else:
#         print("匹配失败！")


# # 简单实例
# str01 = '张三出生于1997年12月20日'
# str02 = '李四出生于1989-01-20'
# str03 = '王五出生于1997/2/5'
# str04 = '赵六出生于1997.12.20'
# str = [str01, str02, str03, str04]
# # 提取出姓名+出生日期
# # 匹配模式
# reg_str12 = '(.*)出生于(\d{4})[.年/-](\d{1,2})[.月/-](\d{1,2}).*?'
# for i in range(4):
#     regtest_test(reg_str12, str[i])

import re

nums = []
with open(r'F:\123\python-practise\Pyhon100Cases\1.txt', encoding='gbk') as f:
    for f1 in f:
        num = re.findall(r"\d+\d*", f1)
        nums.append(num)
print(nums)



