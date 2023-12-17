import pandas as pd
import os

os.chdir(r"文件夹")
df =pd.read_excel(r"文件路径.xls",dtype=str)
class_list = list(df['班级'].drop_duplicates())
longth = len(class_list)  # 计算共有多少数量
path = './SplitExcel'
if not os.path.exists(path):  # 当前文件夹下是否有此文件夹
    os.mkdir(path)  # 创建此文件夹
for i in class_list:
    banji = df[df['班级']==i]
    banji.to_excel('./SplitExcel/%s.xlsx'%(i),index = False)
print('\n{}个名称已经全部拆分完毕，请前往SplitExcel文件夹下查看拆分后的各文件数据.'.format(longth))
print('拆分表格已完成，请到工作目录下查看！')
