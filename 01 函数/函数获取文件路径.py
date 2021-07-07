# *-* conding:utf-8 *-*
import os

'''
def get_file_path(filepath):
    wholepath = []
    for root, dirs, filenames in os.walk(filepath):
        for filename in filenames:
            wholepath.append(os.path.join(root, filename))

    return wholepath


print(get_file_path(r"D:\test1"))
'''


def get_file_path(filepath):
    '''
    获取完整文件路径
    把文件路径输出到指定文件保存
    '''
    wholepath = []
    t = ''
    for root, dirs, filenames in os.walk(filepath):
        for filename in filenames:
            wholepath.append(os.path.join(root, filename))
    with open(r'd:\test1\1.txt', 'w+') as f:
        for i in wholepath:
            f.write(i)
            f.write('\n')


print(get_file_path(r"D:\test1"))
