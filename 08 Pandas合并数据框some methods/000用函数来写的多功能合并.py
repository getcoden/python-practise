import os
import sys
import xlrd
import xlsxwriter
import pandas as pd


def get_file_list(dir, file_type_list=['txt', 'csv', 'xlsx', 'xls'], file_list=[]):
    '''
    获取指定文件夹下指定类型文件路径
    :param dir: 文件夹路径
    :param file_type_list: 文件类型
    :param file_list: 文件列表
    :return:
    '''
    for root, _, files in os.walk(dir):
        for file in files:
            file_type = file[file.rfind('.') + 1:]
            if file_type in file_type_list:
                file_list.append(os.path.join(root, file))
    return file_list


def merge_xlsx_files(file_dir_path, out_file_path,
                     file_type_list=['txt', 'csv', 'xlsx', 'xls'],
                     out_file_name='result.xlsx'):
    '''
    合并目录下指定类型的文件
    :param file_dir_path: 文件夹路径
    :param out_file_path:  输出文件夹路径
    :param file_type_list: 需要合并的文件类型
    :param out_file_name:  输出文件名称
    :return:
    '''
    file_paths = get_file_list(file_dir_path, file_type_list)
    if not os.path.exists(out_file_path):
        os.makedirs(out_file_path)
    dfs = []
    for file in file_paths:
        print(f'file={file}')
        dfs.append(pd.read_excel(file))
    df = pd.concat(dfs)
    df.to_excel(os.path.join(out_file_path, out_file_name), index=False)
    print(f'out_file_path={out_file_path}')


if __name__ == '__main__':
    file_dir_path = os.path.join(sys.path[0], r'D:\jupyter notebook\test')
    out_file_path = os.path.join(sys.path[0], r'D:\jupyter notebook\test')
    merge_xlsx_files(file_dir_path, out_file_path, ['xls'])
