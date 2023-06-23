import pandas as pd
import os

in_path = r"D:\天翼云盘下载\对比两个 excel 文件的异同\SplitExcel"
out_path = r"D:\天翼云盘下载\对比两个 excel 文件的异同\FinallExcel"

if not os.path.exists(out_path):
    os.makedirs(out_path)

for filenames in os.walk(in_path):
    for table in filenames[2]:
        file_path = os.path.join(in_path, table)
        file_name = os.path.splitext(table)[0]
        data = pd.read_excel(file_path)
        data = data.drop(data[data.年级 == '年级'].index)
        data.to_excel(out_path + '\\' + file_name + '.xlsx', index=False)
