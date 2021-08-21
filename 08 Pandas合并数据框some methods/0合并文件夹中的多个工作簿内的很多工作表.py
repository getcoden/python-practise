
# 这个是最完善的一个，值得借鉴
# 导入库
import pandas as pd
import os

'''
df = pd.DataFrame()
path_str = r'D:\jupyter notebook\test'

for excel_str in os.listdir(path_str):
    print('需要合并的文件:', path_str+excel_str)

    new_path = os.path.join(path_str, excel_str)
    if os.path.isfile(new_path):
        excel = pd.ExcelFile(new_path)
        for sheet in excel.sheet_names:

            sheet_excel = excel.parse(sheet)
            sheet_excel['test'] = excel_str.split('.')[0]  # 将原工作簿名作为合并后工作表的列
            df = pd.concat([df, sheet_excel])

# 导出到原文件夹

# if os.path.exists(new_str):
#     os.remove(new_str)
new_str = os.path.join(path_str, '合并文件.xlsx')
df.to_excel(new_str, index=False)
print('合并后数据的大小:', df.shape)
print('合并工作已完成，请到原文件夹内查看结果！')

'''
# ——————————————————————————————————————————————————————————————


# iris = pd.read_excel(r"D:\test\xlsx\16-26-39.xlsx", None)  # 读入数据文件
# keys = list(iris.keys())
# # 第三步：数据合并
# iris_concat = pd.DataFrame()
# for i in keys:
#     iris1 = iris[i]
#     iris_concat = pd.concat([iris_concat, iris1])
# iris_concat.to_excel(r"D:\test\xlsx\iris_concat.xlsx", index=False)  # 数据保存路径


# 使用 pandas 将多个具有多个 Sheet 的 excel 文件合并成一个 excel 文件
# import pandas as pd
# import os
# path = r'C:\files'  # 指定文件夹路径
# wj_List = list(os.walk(path))[0][2]  # 所有子文件名
# xls_file = pd.ExcelFile(path+'\\'+wj_List[0])
# sheet_names = xls_file.sheet_names  # 获取excel文件的所有sheet名
# # 设置excel框架，保证多次写入sheet时不会去被覆盖
# writer = pd.ExcelWriter(path+'\\'+'result.xlsx')
# for sheet in sheet_names:
#     dfs = []
#     for fn in wj_List:
#         dfs.append(pd.read_excel(path+'\\'+fn, sheet))
#     pd.concat(dfs).to_excel(writer, sheet, index=False)
# writer.save()
# writer.close()


path = r"D:\test\xlsx"
file_name_li = os.listdir(path)
print(file_name_li)
# 定义文件名集合
all_file_name = set()
# 定义数据列表
all_data_li = []

# 遍历出每个文件名
for file_name in file_name_li:
    # 将文件夹绝对路径 与 文件名进行拼接
    file_path_li = os.path.join(path, file_name)

    all_data = pd.read_excel(file_path_li, sheet_name=None)
    all_data_li.append(all_data)
    for name in all_data:
        all_file_name.add(name)

    # print(all_data_li)
    # print(all_file_name)
# 创建工作薄
writer = pd.ExcelWriter(r"D:\test\xlsx\all_data.xlsx")
# 遍历每个工作表名
for sheet_name in all_file_name:
    data_li = []
    # 遍历数据
    for data in all_data_li:
        n_rows = data_li.append(data[sheet_name])
    # 将同名数据进行拼接
    group_data = pd.concat(data_li)
    # 保存到writer 工作薄中，并指定工作表名为 sheet_name
    group_data.to_excel(writer, sheet_name=sheet_name)
writer.save()
