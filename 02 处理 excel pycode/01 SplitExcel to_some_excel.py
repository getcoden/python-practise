
import pandas as pd
import os

os.chdir(r"D:\天翼云盘下载\对比两个 excel 文件的异同")
data = pd.read_excel(
    r"D:\天翼云盘下载\对比两个 excel 文件的异同\六年级青骄账号密码.xls")  # 读取数据
data_list = list(data['班级'].drop_duplicates())  # 去重处理
longth = len(data_list)  # 计算共有多少数量
path = './SplitExcel'
if not os.path.exists(path):  # 当前文件夹下是否有此文件夹
    os.mkdir(path)  # 创建此文件夹
count = 0
for item in data_list:
    data_select = data[data['班级'] == item]  # 选出item对应的行
    Bigzone = data_select.iat[0, 0]  # 需要参与文件命名的值
    Smallzone = data_select.iat[0, 1]
    service_code = data_select.iat[0, 2]
    data_select.to_excel(
        './SplitExcel/{0:}-{1:}.xlsx'.format(Bigzone, Smallzone), index=False)  # 按照对应的值生成EXCEL文件
    count += 1
    print('\rEXCEL表中共有 {} 个班级，正在拆分第 {} 个的数据，拆分进度：{:.2%}'.format(
        longth, count, count / longth), end="")
print('\n{}个名称已经全部拆分完毕，请前往SplitExcel文件夹下查看拆分后的各文件数据.'.format(longth))
