# 利用 python 根据路径创建多文件夹及文件夹内容
import os

'''
def mkdir(path):

    # 设置文件夹编号
    Str = "一二三四五六七八"
    for i in Str:

        os.chdir(path)  # 打开要创建文件夹的路径

        name = "第"+i+"套"  # 文件夹名称变量命名

        # 判断文件夹有无后再进行创建文件夹和子文件内容
        isExists = os.path.exists(name)

        if not isExists:  # 如果不存在相同的，则创建文件夹
            os.mkdir(name)
            print(name + "文件夹创建成功")
            os.chdir(path + "/" + name)  # 打开所创建的文件夹
            f = open("错题分析.docx", "w")  # 向文件夹中写入内容
            f.close()  # 记得关闭文件

        else:  # 如果存在相同的，则直接打开该文件夹写入文件即可
            print(name + "文件夹已经存在，正在为你进行下一步......")
            os.chdir(path + "/"+name)
            f = open("错题分析.docx", "w")
            fi = open("text.txt", "w")  # 用于检查else下的代码是否运行
            f.close()
            fi.close()


mkdir(r"C:\Users\win\Desktop\计算机二级模拟试题整理")  # 此处的的斜杠与正常复制的地址路径斜杠方向相反

'''

import os

'''
def mkdir(path):
    folder = os.path.exists(path)
    if not folder:  # 判断是否存在文件夹如果不存在则创建为文件夹
        print("---  创建新的文件夹...  ---")
        os.makedirs(path)  # makedirs 创建文件时如果路径不存在会创建这个路径
        print("---  OK  ---")
    else:
        print("---  文件夹已存在!  ---")


outfile = 'new_folder/test'
folder = os.path.join(os.getcwd(), outfile)
mkdir(folder)  # 调用函数
'''


def mkdir(path):
    folder = os.path.exists(path)
    if not folder:  # 判断是否存在文件夹如果不存在则创建为文件夹
        print("---  创建新的文件夹...  ---")
        os.makedirs(path)  # makedirs 创建文件时如果路径不存在会创建这个路径
        print("---  OK  ---")
    else:
        print("---  文件夹已存在!  ---")


outfile = 'new_folder/test'
folder = os.path.join(os.getcwd(), outfile)
mkdir(folder)  # 调用函数
