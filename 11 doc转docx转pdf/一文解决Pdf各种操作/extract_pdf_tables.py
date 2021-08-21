import os
import pandas as pd
import pdfplumber

'''
def extract_table_info(filepath):
    """
    提取PDF中的图表数据
    @param filepath:
    @return:
    """
    with pdfplumber.open(filepath) as pdf:
        # 获取第18页数据  page = pdf.pages[17]
        page = pdf.pages[0]
        # 如果一页有一个表格，设置表格的第一行为表头，其余为数据
        table_info = page.extract_table()
        df_table = pd.DataFrame(table_info[1:], columns=table_info[0])
        df_table.to_csv('dmeo.csv', index=False, encoding='gbk')


# 提取表格内容
extract_table_info(r"D:\filep\科目.pdf")
'''

'''
上面代码可以获取到第 18 页的第一个表格内容，并且将其保存为 csv 文件存在本地

但是，如果说第 18 页有多个表格内容呢？

因为读取的表格会被存成二维数组，而多个二维数组就组成一个三维数组

遍历这个三位数组，就可以得到该页的每一个表格数据，对应的将 extract_table 函数 改成 extract_tables 即可

具体代码如下：
'''

# 如果一页有多个表格，对应的数据是一个三维数组


def extract_table_info(filepath):
    df_all = []
    with pdfplumber.open(filepath) as pdf:
        # 获取第18页数据  page = pdf.pages[17]
        page = pdf.pages[0]
        # 如果一页有一个表格，设置表格的第一行为表头，其余为数据
        tables_info = page.extract_tables()
        for index in range(len(tables_info)):
            # 设置表格的第一行为表头，其余为数据
            df_table = pd.DataFrame(
                tables_info[index][1:], columns=tables_info[index][0])
            # print(df_table)
            df_all.append(df_table)  # 虽然 df_table 是 Dataframe 格式，但还是要先添加进列表
            df = pd.concat(df_all)  # 将列表内容进行拼接成一个大的 df 才能进行导出
        # print(df)
        df.to_csv(r'D:\filep\dmeo.csv', index=False, encoding='gbk')


# 提取表格内容
extract_table_info(r"D:\filep\d.pdf")
