#!/usr/bin/env python
# -*- coding:utf-8 -*-
# date: 2021/4/17
# filename: xlsx_compare
# author: kplin

import pandas as pd
import os

os.chdir(r"C:\Users\win\Desktop\2")


def my_log(info):
    try:
        with open('error_info.txt', 'w+') as f:
            f.write(info)
            f.close()
    except Exception as e:
        print('写入错误日志时发生以下错误：\n%s' % e)


def get_file():
    try:
        # 获取当前文件夹下的2个文件
        dir_path = os.getcwd()
        files = os.listdir(dir_path)
        ret = []
        for i in files:
            if i.endswith('.xlsx') and not i.endswith('_new.xlsx'):
                ret.append(i)
            if i.endswith('.xlsx') and not i.endswith('_new.xlsx') and '~$' in i:
                info = '请关闭文件%s' % i
                my_log(info)
                return None
        if len(ret) == 0:
            info = '找不到待检测文件，请将2个xlsx文件放入此文件夹'
            my_log(info)
            return None
        # print(ret)
        return ret[0], ret[1]
    except Exception as e:
        my_log(str(e))


def main(file1, file2):
    try:
        # 1、获取原文件路径和名称，先准备即将生成的新文件名和文件路径
        fname1, ext = os.path.splitext(os.path.basename(file1))
        new_file1 = file1.replace(fname1, fname1 + '_new')

        fname2, ext = os.path.splitext(os.path.basename(file2))
        new_file2 = file2.replace(fname2, fname2 + '_new')

        # 2、读取文件
        df1 = pd.read_excel(file1)
        df2 = pd.read_excel(file2)

        length = len(df1) if len(df1) >= len(df2) else len(df2)

        # 两个数据块行数不一致，补成一致的
        if len(df1) - len(df2) > 0:
            # 获取DF1的列名
            d = {}
            for i in df2.columns:
                d[i] = ['' for x in range(len(df1) - len(df2))]
            concat_df = pd.DataFrame(d)
            df2 = pd.concat([df2, concat_df])

        if len(df2) - len(df1) > 0:
            d = {}
            for i in df1.columns:
                d[i] = ['' for x in range(len(df2) - len(df1))]
            concat_df = pd.DataFrame(d)
            df1 = pd.concat([df1, concat_df])

        dis_index = []

        for i in range(len(df1)):
            ret = df1.iloc[i, :] == df2.iloc[i, :]
            if False in ret.tolist():
                dis_index.append(i)

        dis_list = ['' for i in range(length)]
        for i in dis_index:
            dis_list[i] = '不一致'

        df1['Compare Result'] = dis_list
        df2['Compare Result'] = dis_list

        df1.to_excel(new_file1, index=False)
        df2.to_excel(new_file2, index=False)
        my_log('校验成功，本次对比文件为：%s%s 和 %s%s' % (fname1, ext, fname2, ext))
        print('校验完成，请查看新文件')
    except Exception as e:
        print('出现未知错误，请查看error_info.txt')
        my_log(str(e))


if __name__ == '__main__':
    if not get_file():
        print('读取文件时发生错误，请查看error_info.txt')
    else:
        file1, file2 = get_file()
        main(file1, file2)
