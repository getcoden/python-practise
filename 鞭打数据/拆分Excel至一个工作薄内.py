import pandas as pd  #调用pandas包
import xlsxwriter  #调用xlswriter包，用来生成表

data=pd.read_excel('./五年级账号和密码.xls') #读取存储路径在桌面的工作簿chaifengzb,编码格式为gbk
area_list=list(set(data["班级"])) #按分公司字段分成列表

writer=pd.ExcelWriter('./chaifengzb1.xls') #生成一个新 工作簿

data.to_excel(writer,sheet_name="班级",index=False) #将总表存到新工作簿中

for j in area_list:
    df=data[data["班级"]==j]
    df.to_excel(writer,sheet_name=j,index=False) #按分成的列表中的分公司字段进行命名    
writer.save()  #文件保存