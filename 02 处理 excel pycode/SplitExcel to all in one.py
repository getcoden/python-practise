#第一步：调用pandas包
import pandas as pd
#第二步：读取数据
iris = pd.read_excel(r"源文件.xls")#读入数据文件
class_list = list(iris['班级'].drop_duplicates())#获取数据class列，去重并放入列表
# 第三步：按照类别分sheet存放数据
writer = pd.ExcelWriter(r"处理后文件.xls")#创建数据存放路径
for i in class_list: 
    iris1 = iris[iris['班级']==i]
    iris1.to_excel(writer,i)
writer._save()#文件保存

