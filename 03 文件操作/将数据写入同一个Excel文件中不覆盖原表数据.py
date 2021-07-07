from openpyxl import load_workbook
import pandas as pd
import os
import numpy as np
# create some Pandas DateFrame from some data
df1 = pd.DataFrame({'Data1': [1, 2, 3, 4, 5, 6, 7]})
df2 = pd.DataFrame({'Data2': [8, 9, 10, 11, 12, 13]})
df3 = pd.DataFrame({'Data3': [14, 15, 16, 17, 18]})

'''
xls = pd.read_excel(r"D:\test1\test1.xlsx")
# print(xls.sheet_names)

# sheet_to_df_map = {}
for sheet_name in xls.sheet_names:
    #     sheet_to_df_map[sheet_name] = xls.parse(sheet_name)
    # print(sheet_to_df_map)
    for i in xls:
        df11 = pd.read_excel(i)
        print(dff1)
'''

# path = r"D:\test1\test1.xlsx"

# x1 = np.random.randn(100, 2)
# df1 = pd.DataFrame(x1)

# x2 = np.random.randn(100, 2)
# df2 = pd.DataFrame(x2)

# writer = pd.ExcelWriter(path, engine='openpyxl')
# df1.to_excel(writer, sheet_name='x1')
# df2.to_excel(writer, sheet_name='x2')
# writer.save()
# writer.close()
path = r"D:\test1\test1.xlsx"

book = load_workbook(path)
writer = pd.ExcelWriter(path, engine='openpyxl')
writer.book = book

x3 = np.random.randn(100, 2)
df3 = pd.DataFrame(x3)

x4 = np.random.randn(100, 2)
df4 = pd.DataFrame(x4)

df3.to_excel(writer, sheet_name='x31')
df4.to_excel(writer, sheet_name='x42')
writer.save()
writer.close()
