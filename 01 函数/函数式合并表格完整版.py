import pandas as pd 
import numpy as np
import random
data={'a':random.randint(10,21),'b':random.randint(20,31)}
df=pd.DataFrame(data,index=range(1,11))
df
df1=df.copy()
df1


import os

df=pd.DataFrame()
file=os.listdir('d:\\test1')
for i in file:
    if i[-5:]=='.xlsx':
        df_=pd.read_excel('d:\\test1\\{}'.format(i))
        df['filename']=i
        df=df.append(df_)
# print(df)
df.to_excel('d:\\test1\\result.xlsx',index=0)




def get_file(filePath):
    allfilenames=[]
    for root,dirs,filenames in os.walk(filePath):
        for filename in filenames:
            if filename[-5:]=='.xlsx' or filename[-4:]=='.xls':
                wholePath=os.path.join(root,filename)
                allfilenames.append(wholePath)
    return allfilenames


def Get_df(file_dir_path):
    all_df=[]
    for file in file_dir_path:
        df=pd.read_excel(file,0)
        df['File']=file
        all_df.append(df)
        big_df=pd.concat(all_df)
    return big_df

def save_df(bigdf,filename):
    bigdf.to_excel(path,+ '\\' + filename,+ '.xlsx',index=False)


path=r"D:\test1"
alllist=get_file(path)

print(Get_df(alllist))

# print(get_file(path))
# df_list=[fname for fname in os.listdir('d:\\test1\\') if fname[-5:]=='.xlsx']







≤‚ ‘”√
path=r'd:\test1'
filelist=os.listdir(path)
all_df=[]
for files in filelist:
    if files[-5:]=='.xlsx':
        wholepath=os.path.join(path,files)
        df=pd.read_excel(wholepath)
        df['file']=wholepath
        # print(df)
        all_df.append(df)
        big_df=pd.concat(all_df)
print(big_df)
big_df.to_excel(r'd:\test1\re.xlsx',index=False)