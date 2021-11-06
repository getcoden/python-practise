import pandas as pd
import os

in_path = r"C:\Users\star\Desktop\SplitExcel"
out_path = r"C:\Users\star\Desktop\FinalExcel"
if not os.path.exists(out_path):
    os.makedirs(out_path)

for filenames in os.walk(in_path):
    for table in filenames[2]:
        file_path = os.path.join(in_path, table)
        file_name = os.path.splitext(table)[0]
        data = pd.read_excel(file_path, header=0)
        data = data.dropna(axis=1, how='all')
        data.to_excel(out_path+'\\'+file_name+'.xlsx', index=False)
print('done!')
