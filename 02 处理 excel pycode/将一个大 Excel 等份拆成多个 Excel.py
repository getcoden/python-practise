import pandas as pd
import os

# 1. 将一个大 Excel 等份拆成多个 Excel
'''
work_dir = r"D:\test1"
splits_dir = f'{work_dir}/splits'
if not os.path.exists(splits_dir):
    os.mkdir(splits_dir)
df_source = pd.read_excel(f'{work_dir}/baby_trade_history.xlsx')
# print(df_source.head())
total_row_count = df_source.shape[0]
user_names = ['xiao_ming', 'xiao_wang',
              'xiao_wang1', 'xiao_wang2', 'xiao_wang3']
split_size = total_row_count // len(user_names)
if total_row_count % len(user_names) != 0:
    split_size += 1
# print(splits_size)
df_subs = []
for idx, user_name in enumerate(user_names):
    # iloc的开始索引
    begin = idx*split_size
    # iloc的结束索引
    end = begin+split_size
    # 实现df按照iloc拆分
    df_sub = df_source.iloc[begin:end]
    # 将每个子df存入列表
    df_subs.append((idx, user_name, df_sub))


for idx, user_name, df_sub in df_subs:
    file_name = f"{splits_dir}/baby_trade_history_{idx}_{user_name}.xlsx"
    df_sub.to_excel(file_name, index=False)
'''

# 2. 将多个小 Excel 合并成一个大 Excel 并标记来源

work_dir = r"D:\test1"
splits_dir = f'{work_dir}/splits'
# 遍历文件夹，得到要合并的 Excel 名称列表
excel_names = []
for excel_name in os.listdir(splits_dir):
    excel_names.append(excel_name)
# 分别读取到 dataframe
df_list = []
for excel_name in excel_names:
    excel_path = f"{splits_dir}/{excel_name}"
    df_split = pd.read_excel(excel_path)
    # 得到 username
    username = excel_name.replace(
        'baby_trade_history_', '').replace('.xlsx', '')
    # 给每个 df 添加一列，即用户名字
    df_split['username'] = username
    df_list.append(df_split)
df_merged = pd.concat(df_list)
print(df_merged['username'].value_counts())
df_merged.to_excel(f'{work_dir}/baby_trade_history_merged.xlsx', index=False)
