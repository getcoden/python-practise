import shutil
import xlrd
import pandas as pd
import os


def getFile(path):
    dirlst = []
    dirs = os.listdir(path)
    for i in dirs:
        file = os.path.splitext(i)[0]
        if file.startswith('16-'):
            filename = path + '\\' + file+'.xlsx'
            dirlst.append(filename)
    return dirlst


def hebing(csv_list, outputfile):
    for inputfile in csv_list:
        f = open(inputfile)
        data = pd.read_excel(f, encoding='utf8')
        data.to_csv(outputfile, mode='a', index=False)
    print('完成合并')


def quchong(file):
    df = pd.read_excel(file, header=None)
    datalist = df.drop_duplicates()
    datalist.to_csv('D:\\pycharmproject\\result_new.csv',
                    index=False, header=False)
    print('完成去重')


# if __name__ == '__main__':
    # path = r'd:\test\xlsx'
    # dirlst = getFile(path)
    # output_csv_path = 'D:\\test\\xlsx\\result.xlsx'
    # hebing(dirlst, output_csv_path)
    # quchong(output_csv_path)


'''
def file_name(file_dir):
    for root, dirs, files in os.walk(file_dir):
        return files  # 当前路径下所有非目录子文件


# 例如D:/jupyter/test/data
path = input('请键入需要整理的文件夹地址：')
sheet_name = input('请键入要复制的sheet表名字：')
m = input('请键入要复制的单元格所在行数：')
n = input('请键入要复制的单元格所在列数：')

files = file_name(path)


result = pd.DataFrame(columns=['file', 'value'])

for i in range(0, len(files)):
    data = xlrd.open_workbook(path+'/'+files[i])
    print(path+'/'+files[i])
    table = data.sheet_by_name(sheet_name)
    cell = table.cell(int(m), int(n)).value
    result.loc[i] = [files[i], cell]

result.to_csv(path + '/result.csv')
'''

# 导入要用到的相关包
# 合并文件名有规律的工作簿 (union1.py)：

'''
print('请输入待合并工作簿文件所在的路径：')
path = input()      # 待输入合并工作簿总的路径
data = []                                       # 构造一个用于存放数据的空列表
for i in range(1, 5):
    wk_n = path + '/' + str(i) + '.xlsx'  # 构造每个待合并工作簿的路径
    xlsx = xlrd.open_workbook(wk_n)             # 打开工作簿
    sht1 = xlsx.sheet_by_index(0)               # 找到第一个工作表
    nrow = sht1.nrows                           # 提取工作簿中第一个工作表中的数据行数
    title = sht1.row_values(0)                  # 查看工作表中的第一行数据
    for j in range(1, nrow):                     # 将工作表中的每行数据依次添加到列表data中
        data.append(sht1.row_values(j))

# 将列表data转化为DataFrame对象
content = pd.DataFrame(data)

# 修改DataFrame对象的标题
content.columns = title

# 将DataFrame对象content写入新的Excel工作簿中
content.to_excel(path+'\\py_union.xlsx', header=True, index=False)

print('合并完成！')
'''

# 合并文件名无规律的工作簿 (union2.py)：
# 导入要用到的相关包

# 构造获取所有需要合并的工作簿路径并生成路径列表的函数


def file_name(file_dir):
    list = []   # 构造一个用于存放文件名(包括扩展名)的空列表
    for file in os.listdir(file_dir):              # 遍历文件夹file_dir下的所有文件
        if os.path.splitext(file)[1] == '.xlsx':   # 筛选出扩展名是.xlsx的所有文件
            # 将文件扩展名是.xlsx的所有文件的文件名存放到列表list中
            list.append(file)
    return list


print('请输入待合并工作簿文件所在的路径：')
path = input()      # 待输入合并工作簿总的路径
# 通过file_name函数获取path路径下所有xlsx文件的文件名
wks = file_name(path)

data = []  # 定义一个空列表对象
for i in range(len(wks)):
    read_xlsx = xlrd.open_workbook(
        path + '\\' + wks[i])   # 根据path和文件名合并每个待合并工作簿的路径
    sheet1 = read_xlsx.sheets()[0]                         # 找到工作簿中的第一个工作表
    nrow = sheet1.nrows                                   # 提取出第一个工作表中的数据行数
    title = sheet1.row_values(0)                           # 提取出第一个工作表中的表头
    for j in range(1, nrow):                                # 逐行将工作表中的数据添加到空列表data中
        data.append(sheet1.row_values(j))

# 将列表data转化为DataFrame对象
content = pd.DataFrame(data)

# 修改DataFrame对象的标题
content.columns = title

# 将DataFrame对象content写入新的Excel工作簿中
content.to_excel(path+'\\py_union2.xlsx', header=True, index=False)

print('合并完成！')
