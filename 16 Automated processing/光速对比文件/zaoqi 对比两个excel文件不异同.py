import pandas as pd
import numpy as np
import os

os.chdir(r"C:\Users\win\Desktop\1")

df1 = pd.read_excel('iris.xlsx')
df2 = pd.read_excel('iris - 副本.xlsx')
comparison_values = df1.values == df2.values
rows, cols = np.where(comparison_values == False)
for item in zip(rows, cols):
    df1.iloc[item[0], item[1]] = '{} --> {}'.format(
        df1.iloc[item[0], item[1]], df2.iloc[item[0], item[1]])
df1.to_excel('diff.xlsx', index=False, header=True)
print('对比Excel保存成功')
