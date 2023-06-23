from numpy.core.fromnumeric import _put_dispatcher
import pandas as pd
import os


dir_path = r"D:\天翼云盘下载\对比两个 excel 文件的异同\e"
dfs = []
for filenames in os.walk(dir_path):
    for table in filenames[2]:
        path = filenames[0] + '/' + table
        dfs.append(path)

for file in (dfs):
    df_org = pd.read_excel(file, header=None)  # 读取每个文件，以无表头格式读取
    df_org = df_org.dropna(axis=0, how='all')  # 删除每列为空值的空列 axis=0 为删除空行
    df_org.columns = ['年级', '班级', '学生姓名', '账号', '密码']   # 添加列名
    print(df_org.head(5))
    df_org.to_excel(file, index=False)   # 保存每一个文件至原表
