'''
问题：
有一个DataFrame，列名为：['$a', '$b', '$c', '$d', '$e']
现需要改为：['a', 'b', 'c', 'd', 'e']
有何办法？
'''
import pandas as pd
df = pd.DataFrame({'$a': [1], '$b': [1], '$c': [1], '$d': [1], '$e': [1]})
print(df)
'''
解决：

方式一：columns属性
'''
# ①暴力
df.columns = ['a', 'b', 'c', 'd', 'e']
print(df)
# ②修改
df.columns = df.columns.str.strip('$')
print(df)
# ③修改
df.columns = df.columns.map(lambda x: x[1:])
print(df)

'''
方式二：rename方法、columns参数
'''
# ④暴力（好处：也可只修改特定的列）
df.rename(columns={'$a': 'a', '$b': 'b', '$c': 'c', '$d': 'd', '$e': 'e'}, inplace=True)
print(df)
# ⑤修改
df.rename(columns=lambda x: x.replace('$', ''), inplace=True)
print(df)
