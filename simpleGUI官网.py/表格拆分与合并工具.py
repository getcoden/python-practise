import PySimpleGUI as sg
import os
import pandas as pd
import openpyxl

# 拆分表格


out_path = r".\SplitExcel"
if not os.path.exists(out_path):
    os.mkdir(out_path)


def splitTable(df, _key):
    print('----------正在进行表格拆分----------')
    # df = df.astype('str')
    # 按照品牌进行分组
    grouped = df.groupby(by=_key)
    # 输出分组数据导出成单表
    for num, (i, data) in enumerate(grouped):
        data.to_excel(f'.\\{i}.xlsx', index=False, sheet_name=i)
        print(f'已经拆成{num+1}张表格...')

# 合并表格


def concatTable(folder):
    print('----------正在进行表格合并----------')
    # 新建一个空列表，用于存储表格数据
    fileList = []
    # 把文件夹下表格数据放在一个列表里
    for fileName in os.walk(folder):
        for table in fileName[2]:
            path = fileName[0] + '\\' + table
            if os.path.splitext(path)[1] in ('.xlsx', '.xls'):
                li = pd.read_excel(path)
                fileList.append(li)
                print(f'已读取{len(fileList)}个表格...')
            else:
                continue
    # 用concat方法合并表单数据
    result = pd.concat(fileList)
    # 导出数据
    result.to_excel(r'.\合并后文件.xlsx', index=False, sheet_name='汇总')


# 主题设置
sg.theme('LightBrown3')

# 布局设置
layout = [[sg.Text('选择待拆分的文件:', font=("微软雅黑", 12)), sg.InputText(key='file', size=(60, 1), font=("微软雅黑", 10), enable_events=True), sg.FileBrowse('打开', file_types=(("Text Files", "*.xls*"),), font=("微软雅黑", 12))],
          [sg.Text('选择待拆分的字段:', font=("微软雅黑", 12)), sg.Combo('', tooltip='选择用于拆分的字段', font=(
              "微软雅黑", 10), default_value='', auto_size_text=True, size=(15, 5), key='-keys-'), sg.Button('开始拆分', font=("微软雅黑", 12))],
          [sg.Text('选择待合并文件夹:', font=("微软雅黑", 12)), sg.InputText(key='Folder', size=(60, 1), font=(
              "微软雅黑", 10), enable_events=True), sg.FolderBrowse('打开文件夹', font=("微软雅黑", 12)), sg.Button('开始合并', font=("微软雅黑", 12))],
          [sg.Text('程序操作记录:', justification='center')],
          [sg.Output(size=(100, 10), font=("微软雅黑", 10))],
          [sg.Text('操作说明:', font=("微软雅黑", 12))],
          [sg.Text('表格拆分指引：选择文件—>选择用于拆分的字段—>开始拆分—>结果文件在本程序所在文件夹内\n表格合并指引：选择需要合并的表格所在文件夹—>开始合并—>结果文件在本程序所在文件夹内', font=("微软雅黑", 10)), sg.Text(
              '', font=("微软雅黑", 12), size=(20, 1)), sg.Button('关闭程序', font=("微软雅黑", 12), button_color='red')]
          ]

# 创建窗口
window = sg.Window('Excel 表格拆分与合并工具，制作：拂晓  6年级(8)班，张悦   指导：张 飞', layout,
                   font=("微软雅黑", 12), icon=r"D:\sourcedata\Student made\Excel 拆分与合并\Excel.ico", default_element_size=(50, 1))

# 事件循环
while True:
    event, values = window.read()
    if event in (None, '关闭程序'):
        break
    if event == 'file':
        fileName = values['file']
        if os.path.exists(fileName):
            df = pd.read_excel(fileName)
            keys = df.columns.to_list()
            window["-keys-"].Update(values=keys,
                                    font=("微软雅黑", 10), size=(15, 8))
        else:
            print('文件不存在\n请先选择正确文件')
    if event == '开始拆分':
        if values['-keys-']:
            _key = values['-keys-']
            splitTable(df, _key)
            print('----------拆分工作已经完成----------\n')
        else:
            print('字段未选择-请先选择字段\n或文件未选取-请先选择文件')
    if event == '开始合并':
        if values['Folder']:
            folder = values['Folder']
            concatTable(folder)
            print('----------合并工作已经完成----------\n')
        else:
            print('待合并文件所在文件夹未选择')

window.close()
