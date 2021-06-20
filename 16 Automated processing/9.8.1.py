'''
选择性拷贝
项目要求：编写一个程序，遍历一个目录树，查找特定扩展名的文件（诸如.pdf 或.jpg），
不论这些文件的位置在哪里， 将它们拷贝到一个新的文件夹中。
'''
#! python3
# selective copy

import os
import shutil
os.chdir("D:\pdf")
# to generate a file, and make sure the file has not existed
try:
    os.makedirs('copy_to_this_dir')
except FileExistsError:
    pass
# walk throgh a dir and find particular file, like '.pdf','.txt', etc.
for root, dirs, files in os.walk('.'):
    for file in files:
        # what kind of file that you want to copy
        if file.endswith('.pdf') or file.endswith('.txt'):
            # 这一步很重要，是为了排除自己复制成自己（因为os.walk的直线遍历性）
            if file not in os.listdir('copy_to_this_dir'):
                # copy these files to a new folder
                shutil.copy(os.path.join(root, file), 'copy_to_this_dir')
