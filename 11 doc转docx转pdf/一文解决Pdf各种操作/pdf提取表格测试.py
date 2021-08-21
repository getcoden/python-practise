import csv
import math
import importlib
import sys
import os
import pdfplumber
import pandas as pd


sheetname = ['考古文博', '历史学', '马克思主义理论', '555']
# 读取pdf文件，返回pdfplumber.PDF类的实例
pdf = pdfplumber.open(r"D:\filep\d1.pdf")
writer = pd.ExcelWriter(r"D:\filep\output3.xlsx")
# 第二页pdfplumber.Page实例
df_all = pd.DataFrame()
for pages in pdf.pages[0:2]:

    for table in pages.extract_tables():
        # print(table)
        table_df = pd.DataFrame(table[1:], columns=['语文', '数据不', '右', '顺',
                                                    '中成药', '三国杀', '口', '中', '交', '顺'])
        df_all = df_all.append(table_df)

new_df = pd.DataFrame()
j = 1
index = []
# 记录序号==1的行索引，用于后面的表格拆分
for i in range(len(df_all)):
    if df_all.iloc[i, 0] == '0':
        index.append(i)
        print("################")
index.append(len(df_all))
print(index)

# 按行索引将内容切片并逐个添加到表中
for t in range(len(index)-1):
    new_df = df_all.iloc[index[t]:index[t+1]-1, :]
    print(new_df)
    new_df.to_excel(
        writer, sheet_name=sheetname[t], encoding='gb2312', index=None)


writer.save()
print('finished')


'''
python 中有很多库可以处理 pdf，比如 PyPDF2、pdfminer 等，那 pdfplumber 的优势在哪呢？

首先，pdfplumber 能轻松访问有关 PDF 对象的所有详细信息，且用于提取文本和表格的方法高级可定制，使用者可根据表格的具体形式来调整参数。

最关键的是 pdfplumber 作者持续在维护该库，而同样受欢迎的 PyPDF2 已经不再维护了。
'''
