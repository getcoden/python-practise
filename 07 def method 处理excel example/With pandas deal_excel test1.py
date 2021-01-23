# 一个表一个班级+学科组合，表内数据按照分数段分组
# 思路：分组保存之循环思想
import pandas as pd
import numpy as np
from pandas.api.types import CategoricalDtype
data = pd.read_excel(r'C:\Users\17621802479\Desktop\student.xlsx',sheet_name='元数据')


# 定义函数，参数包括数据，班级，学科
# 此函数用于得到对应上班级、学科得学生数据，加了一列分数段
# 后续循环各个班级和学科，调用此函数进行循环保存到工作表
def groupByClassAndSubject(data,clazz,subject):
    data1=data.loc[data['班级']==clazz,['考号','班级','姓名','性别',subject,'电话']]
    data1['分数段'] = pd.cut(data1[subject], [0, 60, 80, 90, 100, float('inf')],
                            labels=['<=60分', '61-80分', '81-90分', '90-100分','100分以上'])
    # 自定义排序规则
    data1['分数段'] = data1['分数段'].astype(CategoricalDtype(categories=['<=60分', '61-80分', '81-90分', '90-100分','100分以上'], ordered=True))
    # 排序
    data1=data1.sort_values(by='分数段')
    # 将分数段这一列放到第一列来
    data1=data1.reindex(columns=['分数段','考号','班级','姓名','性别',subject,'电话'])
    return data1

# 循环条件
clazz=data['班级'].drop_duplicates().sort_values()
subject=['语文','数学','英语']

writer = pd.ExcelWriter(r'C:\Users\17621802479\Desktop\student.xlsx')
# 因为待会保存时，元数据会被覆盖，因此先把元数据保存下
data.to_excel(excel_writer=writer, sheet_name='元数据', index=False)

# 循环
for clazz1 in clazz:
    for subject1 in subject:
        data1=groupByClassAndSubject(data,clazz1,subject1)
        # 保存到不同得工作表，工作表是sheet_name=clazz1+'-'+subject1组合而已
        data1.to_excel(excel_writer=writer,sheet_name=clazz1+'-'+subject1,index=False)

# 保存、关闭
writer.save()
writer.close()