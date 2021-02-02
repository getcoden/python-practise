import pandas as pd

df = pd.ExcelFile('your_file')

df_new = pd.DataFrame()

for name in df.sheet_names:  # 获取每个Sheet的名称
    # 循环读取每个Sheet表内容，同时设置某列为字符串，避免长数字文本被识别为数字
    df_pre = df.parse(sheet_name=name, dtype={'columns_name': str})
    df_new = df_new.append(df_pre)

df_new.to_excel('your_newfile')
