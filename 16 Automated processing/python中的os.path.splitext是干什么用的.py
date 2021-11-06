# 作用 ：分离文件名与扩展名；默认返回(fname, fextension)元组，可做分片操作 。

# 比如：

import os

path_01 = r"C:\Users\win\Desktop\2\try - 副本.xlsx"

path_02 = r"C:\Users\win\Desktop\2\try.xlsx"

root_01 = os.path.splitext(path_01)

root_02 = os.path.splitext(path_02)

print(root_01[0])

print(root_02[0])

# python中的os.path模块用法：
'''
dirname()   # 用于去掉文件名，返回目录所在的路径
# 如：


os.path.dirname('d:\\library\\book.txt')
'd:\\library'

basename()   # 用于去掉目录的路径，只返回文件名
# 如：


os.path.basename('d:\\library\\book.txt')
'book.txt'

join()   # 用于将分离的各部分组合成一个路径名
# 如：


os.path.join('d:\\library', 'book.txt')
'd:\\library\\book.txt'

split()  # 用于返回目录路径和文件名的元组
# 如：


os.path.split('d:\\library\\book.txt')
('d:\\library', 'book.txt')

splitdrive()    # 用于返回盘符和路径字符元组


os.path.splitdrive('d:\\library\\book.txt')
('d:', '\\library\\book.txt')
splitext()    # 用于返回文件名和扩展名元组

# 如：

os.path.splitext('d:\\library\\book.txt')
('d:\\library\\book', '.txt')

os.path.splitext('book.txt')
('book', '.txt')
'''
