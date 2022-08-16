# -*- coding: utf-8 -*-
import os
import pandas as pd
import numpy as np

df = pd.read_excel(r"D:\sourcedata\Student made\Excel 拆分与合并\test_测试文件.xlsx")

data = pd.np.array(df)
data_ = data.tolist()

arr = []
# print(data_[0][1])
for i in data_:
    item = i[3]
    arr.append(item)
# print(arr)
    l = ','.join(arr)
print(l)
