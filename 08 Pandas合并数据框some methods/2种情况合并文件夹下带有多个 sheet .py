#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2018/5/31 0031 15:29
# @Author  : 一梦南柯
# @File    : data_process1.py


'''
使用pandas读取.xlxs的excel多个sheet文件，并且写出csv格式的excel文件
'''
import time
import os
import pandas as pd

# def excel_add(file_path):
#     xls_file = pd.ExcelFile(file_path)
#     # 显示出读入excel文件中各个sheet表的名字
#     sheet_names = xls_file.sheet_names
#     df_all = []
#     for i in sheet_names:
#         # skiprows=0代表读取跳过的行数为0行，不写代表不跳过标题
#         df = pd.read_excel(file_path, sheet_name=i)
#         df_all.append(df)
#         df1 = pd.concat(df_all)
#     # print(df1)
#     # 第一个参数是说把dataframe写入到D盘下的TEST2.csv文件中，参数sep表示字段之间用’, ’分隔，header表示是否需要头部，index表示是否需要行号。
#     df1.to_excel(r"D:\test\xlsx" + '\\rusult.xlsx', index=False)


# if __name__ == '__main__':
#     file_path = r"D:\test\xlsx\1.xlsx"
#     excel_add(file_path)


# 如果只读文件夹下所有多 sheet 的 excel 文件，见代码 2
# 代码 2：
#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2018/5/31 0031 15:29
# @Author  : 一梦南柯
# @File    : data_process1.py


'''
使用pandas读取文件夹下全部带有多个sheet的.xlxs文件，并且写出csv格式的excel文件
例子：若文件夹中有2个文件，则第一个for循环后，输出为：
D:\5.3\test
[]
['test.xlsx', 'test2.xlsx']
'''


def excel_add(file_path):
    time1 = time.time()
    InputDir = file_path
    rootdir = InputDir
    df_all = []
    for parent, dirnames, filenames in os.walk(rootdir):
        for filename in filenames:
            xls_file = pd.ExcelFile(os.path.join(parent, filename))
            # 显示出读入excel文件中各个sheet表的名字
            sheet_names = xls_file.sheet_names
            for i in sheet_names:
                # skiprows=0代表读取跳过的行数第0行，不写代表不跳过标题
                df = pd.read_excel(os.path.join(
                    parent, filename), sheet_name=i)
                df_all.append(df)
                df2 = pd.concat(df_all)
  # 第一个参数是说把dataframe写入到D盘下的TEST2.csv文件中，参数sep表示字段之间用’, ’分隔，header表示是否需要头部，index表示是否需要行号。
    df2.to_excel(r"D:\test\xlsx" + '\\rusult2.xlsx',
                 header=True, index=False)
    time2 = time.time()
    time3 = time2-time1
    print(time3)


if __name__ == '__main__':
    #file_path = 'D:\\5.3\\test'
    file_path = r"d:\test\xlsx"
    excel_add(file_path)
