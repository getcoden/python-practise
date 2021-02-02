
# 这个是最完善的一个，值得借鉴
# 导入库
import pandas as pd
import os

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
