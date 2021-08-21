

import win32com.client as win32
import os
import sys
import pandas as pd
from datetime import datetime


def displaydir(dir_path):
    file_list = []
    n = 0
    for filenames in os.walk(dir_path):
        for table in filenames[2]:
            path = filenames[0] + '/' + table
            li = pd.read_excel(path)
            li['file_name'] = os.path.splitext(table)[0]
            n += 1
            file_list.append(li)
            print(' 第' + str(n) + ' 个表格已合并')
    print('在该目录下有 %d 个 xlsx 文件' % len(file_list))
    data_result = pd.concat(file_list, ignore_index=True)
    data_result.to_excel(out_path + '/' + 'result.xlsx', index=False)


if __name__ == "__main__":
    dir_path = r"D:\test\xlsx"
    out_path = r"C:\Users\win\Desktop\xlsx"
    if not os.path.exists(out_path):
        os.makedirs(out_path)

    displaydir(dir_path)


# 批量转换文件xls-xlsx


def xls2xlsx():
    rootdir = r"D:\test\excel\data"  # 需要转换的xls文件存放处
    rootdir1 = r"D:\test\excel\data\ex"  # 转换好的xlsx文件存放处
    files = os.listdir(rootdir)  # 列出xls文件夹下的所有文件
    num = len(files)  # 列出所有文件的个数
    for i in range(num):  # 按文件个数执行次数
        # 分离文件名与扩展名，返回(f_name, f_extension)元组
        kname = os.path.splitext(files[i])[1]
        if kname == '.xls':  # 判定扩展名是否为xls,屏蔽其它文件
            fname = rootdir + '\\' + files[i]  # 合成需要转换的路径与文件名
            fname1 = rootdir1 + '\\' + files[i]  # 合成准备存放转换好的路径与文件名
            excel = win32.gencache.EnsureDispatch(
                'Excel.Application')  # 调用win32模块
            wb = excel.Workbooks.Open(fname)  # 打开需要转换的文件
            wb.SaveAs(fname1+"x", FileFormat=51)  # 文件另存为xlsx扩展名的文件
            wb.Close()
            excel.Application.Quit()


if __name__ == '__main__':
    xls2xlsx()
