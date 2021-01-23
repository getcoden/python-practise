import xlutils
import xlwt
import xlrd
import openpyxl
import pandas as pd
import pandas as pd

# 方法一

df1 = pd.DataFrame({'A': [1, 2, 3, 4]})
df2 = pd.DataFrame({'B': [1, 2, 3, 4]})
xlsx = pd.ExcelWriter('./test.xlsx')
df1.to_excel(xlsx, sheet_name='df1')
df2.to_excel(xlsx, sheet_name='df2')
xlsx.close()


# 方法二

df1 = pd.DataFrame({'a': [3, 1], 'b': [4, 3]})  # 随机生成一个DataFrame 数据
df2 = df1.copy()
with pd.ExcelWriter('output.xlsx') as writer:
    for i in range(1, 4):
        name = 'Sheet_name_'+str(i)
        df1.to_excel(writer, sheet_name=name)
#       df2.to_excel(writer, sheet_name='Sheet_name_2')


# 函数方式保存

x_1 = pd.DataFrame({'A': [1, 2, 3, 4]})


def write_excel(dataframe, excelWriter, sheetname):
    """
    数据写入到Excel,可以写入不同的sheet
    """
    book = openpyxl.load_workbook(excelWriter.path)
    excelWriter.book = book
    dataframe.to_excel(excel_writer=excelWriter,
                       sheet_name=sheetname, index=None)
    excelWriter.close()


excelPath = 'D:/data.xlsx'
excelWriter = pd.ExcelWriter(excelPath, engine='openpyxl')
write_excel(x_1, excelWriter, 'b')
