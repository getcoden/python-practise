import pandas as pd
import os

# 读取数据并指定从第几行开始读，例 header=4 即从第4行开始读，以便跳过合并单元格的表头
data = pd.read_excel(
    r"D:\天翼云盘下载\对比两个 excel 文件的异同\六年级青骄账号密码.xls", header=0)
data = data.dropna(how='any')  # 删除一行中任意值为空的行 ，all 为一行所有值为空
# data.drop(data.columns[[0, 1]], axis=1, inplace=True)  # 删除指定索引列
# print(data)
data.to_excel(r"D:\天翼云盘下载\对比两个 excel 文件的异同\空行删除完成.xls", index=False)
