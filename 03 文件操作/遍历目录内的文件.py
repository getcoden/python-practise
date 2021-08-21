import os
"""
# (1)

import os
os.getcwd()
path = os.getcwd()
os.listdir(path)


# (2)

result = []


def get_all(cwd):
    get_dir = os.listdir(cwd)
    for i in get_dir:
        sub_dir = os.path.join(cwd, i)
        if os.path.isdir(sub_dir):
            get_all(sub_dir)
        else:
            result.append(i)


if __name__ == "__main__":
    get_all(r'D:\Wowode\jupyterlab\test')
    print(result)
    print('������{}���ļ�'.format(len(result)))

"""
# python 获取某目录下（含子目录）所有文件名称
"""目的：获得某目录下（含子目录）的所有文件的名称。os.listdir 函数只能列举当前目录下的文件名称。
所以参考写了一个递归函数如下(注意因为是递归函数，所以这个 flist 的变量需要在定义的子函数之外。)：
"""

flist = []


def getFlist(path):
    global flist
    lsdir = os.listdir(path)
    dirs = [i for i in lsdir if os.path.isdir(os.path.join(path, i))]
    if dirs:
        for i in dirs:
            getFlist(os.path.join(path, i))
    files = [i for i in lsdir if os.path.isfile(os.path.join(path, i))]
    for file in files:
        flist.append(file)
    return flist

path = r'C:\Users\win\Desktop\ccc'
flist = getFlist(path)
print(flist)


# 还有另外一个更为简单的方法，就是使用 os.walk 函数，代码如下：


# def getFlist(path):
#     for root, dirs, files in os.walk(path):
#         print('root_dir:', root)
#         print('sub_dirs:', dirs)
#         print('files:', files)
#     return files


# resDir = 'C:\\Users\\win\\Desktop\\ccc'
# flist = getFlist(resDir)
