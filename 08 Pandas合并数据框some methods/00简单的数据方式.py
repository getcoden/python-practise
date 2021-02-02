import pandas as pd
import os


Folder_Path = r'D:\jupyter notebook\test'
file_list = os.listdir(Folder_Path)

dfs = []
for item in file_list:
    print('需要合并的文件为:', Folder_Path+item)
    dfs.append(pd.read_excel(Folder_Path + '\\' + item))

df = pd.concat(dfs, sort=False)
df.to_excel(r'D:\jupyter notebook\test\test.xlsx', index=False)
print('合并后的数据大小为:', df.shape)
print('合并完成')


# 这个带进度表

dir = 'test/'
filenames = os.listdir(dir)
index = 0
dfs = []
for name in filenames:
    print('正在处理第' + str(index+1) + '个表格')
    dfs.append(pd.read_excel(os.path.join(dir, name)))
    index += 1
df = pd.concat(dfs)
df.to_excel('test/total.xlsx', index=False)
