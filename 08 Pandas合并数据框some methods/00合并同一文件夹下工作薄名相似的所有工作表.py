# 合并同一文件夹下工作薄名相似的所有工作表，这是最完整的一个

import numpy as np
import pandas as pd
import datetime as dt

import glob
import os
# runDir = r'D:\jupyter notebook\test\11.xlsx'
# if os.getcwd()!=runDir:
#     os.chdir(runDir)
files = glob.glob('11*.xlsx')

df = pd.DataFrame()

for each in files:
    sheets = pd.ExcelFile(each).sheet_names

    for sheet in sheets:
        df = df.append(pd.read_excel(each, sheet, index_col=0))

df.to_excel(r'D:\jupyter notebook\test\1111.xlsx', index=False)
print('数据大小为:', df.shape)
