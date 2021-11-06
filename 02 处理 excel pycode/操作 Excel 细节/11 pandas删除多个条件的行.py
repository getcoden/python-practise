# _*_ conding:utf-8 _*_
import pandas as pd 

df = pd.DataFrame({
    'case_id': [1050, 1050, 1050, 1050, 1051, 1051, 1051, 1051],
    'elm_id': [101, 102, 101, 102, 101, 102, 101, 102],
    'cid': [1, 1, 2, 2, 1, 1, 2, 2],
    'fx': [736.1, 16.5, 98.8, 158.5, 272.5, 750.0, 333.4, 104.2],
    'fy': [992.0, 261.3, 798.3, 452.0, 535.9, 838.8, 526.7, 119.4],
    'fz': [428.4, 611.0, 948.3, 523.9, 880.9, 340.3, 890.7, 422.1]})
print(df)

# df2 = df[(df.case_id != subcase) & (df.cid != commit_id)]
# print(df2)

df3=df.query('(case_id != 1051) & (cid != 1)')
print(df3)


# 删除条件的行
# df.drop(df.loc[(~df['case_id'].isin(cases)) & (~df['cid'].isin(ids))].index)
# print(df)