import pandas as pd
import numpy as np
import openpyxl

# 读取excel 某个sheet下的数据,将其转化为列表数据，方便操作


def get_excel_sheet_data(filename, sheetname):
    try:
        df = pd.read_excel(filename, sheet_name=sheetname)
        dataList = df.to_dict(orient='records')  # 转换为列表
        return dataList
    except:
        print('未能打开此文件，请确认文件名及路径是否正确')
        return []


# 读取excel 所有sheet表名，并将其转化为列表返回
def get_excel_sheet_list(filename):
    try:
        df = pd.read_excel(filename, sheet_name=None)
        return df.keys()
    except Exception as e:
        print(e)
        return []


if __name__ == '__main__':
    fileName = 'D:/test/xlsx/Notes_111.xlsx'
    sheetList = get_excel_sheet_list(fileName)  # 获取sheet列表
    print(sheetList)
    writer = pd.ExcelWriter("D:/test/xlsx/新数据.xlsx", engin='openpyxl')
    for i in sheetList:  # 遍历每个sheet名称
        sheetData = get_excel_sheet_data(fileName, i)   # 读取每个sheet下的数据
        for j in sheetData:  # 取出每一项的数据
            # do something
            # 依次根据sheet名称对“新数据.xlsx”此文件多次写入Sheet
            pd_look = pd.DataFrame(sheetData)
            pd_look.to_excel(writer, sheet_name=i, index=False)
        # 最后保存写入，并释放
    writer.save()
    writer.close()
