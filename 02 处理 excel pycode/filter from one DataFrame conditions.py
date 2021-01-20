
"""
pandas筛选出表中满足另一个表所有条件的数据方法

"""

import pandas as pd

list1 = [['a',1,255,100,'03'],['a',2,481,50,'06'],['a',47,255,500,'03'],['b',3,1,50,'11']]
list2 = [['a','03',255],['a','06',481]]

#将list转化为dataframe

df1=pd.DataFrame(list1,columns=["名字","ID","颜色","数量","类型"])

df2=pd.DataFrame(list2,columns=["名字","类型","颜色"])

#用pandas.merge函数将其进行内连接

df=pd.merge(df1,df2,how='inner',on=["名字","类型","颜色"],right_index=True)

#按索引排序
df.sort_index(inplace=True)
print(df)