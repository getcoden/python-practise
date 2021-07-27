import pandas as pd
from datetime import datetime  # 必须以这种格式导入包


# datapd = pd.read_excel(r"D:\jupyter notebook\test\result.xlsx")
# datapd['出生日期'] = pd.to_datetime(datapd['出生日期'])
# print(datapd['出生日期'])

# 对于这种合成的表格，读取表格后首先要做的就是用 info() 查看每列的数据类型，以便进行后期的进一步处理，避免一些不必要的麻烦

datapd = pd.read_excel(r"D:\jupyter notebook\test\result.xlsx")
datapd['出生日期'] = pd.to_datetime(datapd['出生日期'])  # 先将日期列转换为datetime64类型
datapd['出生日期'] = datapd['出生日期'].apply(
    lambda x: datetime.combine(x, datetime.min.time()))  # 所以在格式化之前，必须将 dates 转换为 datetimes，
datapd['出生日期'] = datapd['出生日期'].dt.strftime("%m/%d/%Y")


print(datapd['出生日期'])
