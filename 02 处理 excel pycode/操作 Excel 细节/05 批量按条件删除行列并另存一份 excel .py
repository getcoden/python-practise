import pandas as pd 
import os 

in_path=r"C:\Users\Lenovo\Desktop\SplitExcel"
out_path = r"C:\Users\Lenovo\Desktop\FinallExcel"

if not os.path.exists(out_path):
    os.makedirs(out_path)

for filenames in os.walk(in_path):
    for table in filenames[2]:
        file_path=os.path.join(in_path,table)
        file_name=os.path.splitext(table)[0]
        data=pd.read_excel(file_path)
        data=data.drop(data[data.年级=='年级'].index)
        data.to_excel(out_path + '\\'+ file_name + '.xlsx',index=False)
