# -*- coding:utf-8*-
import os
import sys
import pandas
from datetime import datetime


# file_path = r"C:\Users\win\Desktop\cishi"
# file_list = os.listdir(file_path)
# full_path_list = []
# for i in file_list:
#     name = os.path.splitext(i)[0]
#     full_path = os.path.join(file_path, i)
#     full_path_list.append(full_path)

# with open('C:/Users/win/Desktop/All_one_txt.txt', 'a+') as f:
#     count = 0
#     for file in full_path_list:
#         with open(file, encoding='gbk') as f1:
#             f.write('\n'+'### ' + name + ' ###'+'\n'+'\n')
#             for zi in f1:
#                 f.write(zi)
#             count += 1
#     print(f'{count}' + ' 个文件已合并！')


def MergeTxt(filepath, outfile):
    count = 0
    k = open(filepath+outfile, 'a+', encoding='utf-8')
    for parent, dirnames, filenames in os.walk(filepath):
        for filepath in filenames:
            name = os.path.splitext(filepath)[0]
            k.write('\n'+'\n' + '### ' + name + ' ###'+'\n'+'\n')
            # k.write(os.path.splitext(filepath)[0])
            txtPath = os.path.join(parent, filepath)  # txtpath就是所有文件夹的路径
            with open(txtPath, encoding='utf-8', errors="ignore") as f:
                k.write('\n')

                ##########换行写入##################
                for line in f:
                    k.write(line)
                count += 1
    k.close()
    print("finished! "+'共计'f'{count}'+'个文件被合并！')


if __name__ == '__main__':
    file_dir = r"C:\Users\win\Desktop\历史收藏"
    outfile = "result.txt"

    MergeTxt(file_dir, outfile)

    print('已完成合并')
