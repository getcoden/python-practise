
# 导入工具包
import pandas as pd
import os
import datetime as dt
import numpy as np

# # 设置文件路径
# path = r"D:\jupyter notebook\test"
# # 空列表, 用于存放文件路径
# files = []
# for file in os.listdir(path):
#     if file.endswith(".xls"):
#         files.append(os.path.join(path, file))

# # 定义一个空的dataframe
# data = pd.DataFrame()

# # 遍历所有文件
# for file in files:
#     datai = pd.read_excel(file, dtype={' 出生日期 ': np.datetime64})  # 在读取文件时就指定日期列的日期格式为np.datetime64
#     datai_len = len(datai)
#     data = data.append(datai)   # 添加到总的数据中
#     print('读取%i行数据,合并后文件%i列, 名称：%s' %
#           (datai_len, len(data.columns), file.split('/')[-1]))
#     # 查看是否全部读取，格式是否出错
# # 重置索引
# data.reset_index(drop=True, inplace=True)
# data.to_excel(r"D:\jupyter notebook\test\result1.xlsx", index=False)

datapd = pd.read_excel(r"D:\jupyter notebook\test\result1.xlsx")
print(datapd.出生日期)
