import pandas as pd

# 读取excel 某个sheet下的数据,将其转化为列表数据，方便操作


# def get_excel_sheet_data(filename, sheetname):
#     try:
#         df = pd.read_excel(filename, sheet_name=sheetname)
#         dataList = df.to_dict(orient='records')  # 转换为列表
#         return dataList
#     except:
#         print('未能打开此文件，请确认文件名及路径是否正确')
#         return []

# # 读取excel 所有sheet表名，并将其转化为列表返回


# def get_excel_sheet_list(filename):
#     try:
#         df = pd.read_excel(filename, sheet_name=None)
#         return df.keys()
#     except Exception as e:
#         print(e)
#         return []


# if __name__ == '__main__':
#     fileName = '数据.xlsx'
#     sheetList = get_excel_sheet_list(fileName)  # 获取sheet列表
#     print(sheetList)
#     writer = pd.ExcelWriter("新数据.xlsx")
#     for i in sheetList:  # 遍历每个sheet名称
#         sheetData = get_excel_sheet_data(fileName, i)   # 读取每个sheet下的数据
#         for j in sheetData:  # 取出每一项的数据
#             # do something
#             # 依次根据sheet名称对“新数据.xlsx”此文件多次写入Sheet
#         pd_look = pd.DataFrame(sheetData)
#         pd_look.to_excel(writer, sheet_name=i)
#         # 最后保存写入，并释放
#     writer.save()
#     writer.close()

# i） 合并同一文件夹下的所有工作簿
import os
import pandas as pd


def concat_xlsx(dir_name, result_filename='result'):
    '''合并同一文件夹下的所有excel工作簿'''
    dfs = []
    for filename in os.listdir(dir_name):
        if os.path.splitext(filename)[1] == '.xlsx':
            full_path = os.path.join(dir_name, filename)
            df = pd.read_excel(full_path)
            dfs.append(df)

    result = pd.concat(dfs)
    result_path = os.path.join(dir_name, result_filename + '.xlsx')
    result.to_excel(result_path, index=False, freeze_panes=(1, 0))

# iii） 合并一个工作簿中的多个工作表


def concat_worksheets(path, result_path):
    '''合并同一工作簿中的所有工作表'''
    dfs = pd.read_excel(path, sheet_name=None).values()
    result = pd.concat(dfs)
    result.to_excel(result_path, index=0, freeze_panes=(1, 0))
