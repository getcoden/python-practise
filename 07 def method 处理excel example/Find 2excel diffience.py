# coding: UTF-8
import pandas as pd
import numpy as np
df1 = pd.read_excel('D:\\test\\1.xlsx')
df2 = pd.read_excel('D:\\test\\2.xlsx')
# df1
# df2[['数据3','数据7']]

# difference = df1[[df1!=df2]]
# difference
comparison_values = df1.values == df2.values
comparison_values
rows, cols = np.where(comparison_values == False)
for item in zip(rows, cols):
    df1.iloc[item[0], item[1]] = '{} --> {}'.format(
        df1.iloc[item[0], item[1]], df2.iloc[item[0], item[1]])
df1
# df1.to_excel(r'D:\test\diff.xlsx',index=False,header=True)
# print('Done!')
