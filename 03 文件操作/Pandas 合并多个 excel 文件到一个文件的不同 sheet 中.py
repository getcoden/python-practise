import pandas as pd
import os
from openpyxl import load_workbook  # 必须导入的模块

path = r"D:\test1\file_folder"
listing = os.listdir(path)
data_list = [f for f in listing if f[-5:] == '.xlsx']  # 为了排除不是.xlsx的文件，避免程序报错

with pd.ExcelWriter(r"D:\test1\result.xlsx", engine='openpyxl') as writer:  # 这是一种高效的写法
    for i in data_list:
        name = i.split('.')[0]
        df1 = pd.read_excel(os.path.join(path, i))
        df1.to_excel(writer, sheet_name=name, index=False)  # 程序的逻辑

# 另一种写法

writer = pd.ExcelWriter(r'result.xlsx')

for i in os.listdir(r'./file_folder'):
    name = i.split('.')[0]
    df1 = pd.read_excel(os.path.join(r'./file_folder', i))
    df1.to_excel(writer, sheet_name=name, index=False)
writer.save()  # 这2个操作不能忘记，否则文件只在缓存里，看不到直接的操作结果
writer.close()


# 获取工作薄所有工作表列表
# 方法一
# df = pd.read_excel(path, sheet_name=None)
# for i in df.keys():
#     print(i)


# 方法二:
# df = pd.read_excel(path, sheet_name=None)
# sheet_name_list = list(df)
# print(sheet_name_list)
