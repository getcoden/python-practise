# -*- coding: UTF8 -*-

from os.path import join, getsize
import os
import datetime
import time
# python 获取文件大小，创建时间和访问时间


''' 把时间戳转化为时间: 1479264792 to 2016-11-16 10:53:12'''


def TimeStampToTime(timestamp):
    timeStruct = time.localtime(timestamp)
    return time.strftime('%Y-%m-%d %H:%M:%S', timeStruct)


# print(TimeStampToTime(1479264792))

''' 获取文件的大小，结果保留两位小数，单位为 MB'''


def get_FileSize(filePath):
    filePath = (filePath)
    fsize = os.path.getsize(filePath)
    fsize = fsize/float(1024*1024)
    return round(fsize, 2)


print(get_FileSize(r"C:\Users\win\Desktop\2\1\0.jpg"))

'''
2、获取文件夹大小，即遍历文件夹，将所有文件大小加和。遍历文件夹使用 os.walk 函数

　　os.walk () 可以得到一个三元 tupple (dirpath, dirnames, filenames)，

　　1、第一个为起始路径，

　　2、第二个为起始路径下的文件夹，

　　3、第三个是起始路径下的文件。

　　其中 dirpath 是一个 string，代表目录的路径，dirnames 是一个 list，包含了 dirpath 下所有子目录的名字。filenames 是一个 list，包含了非目录文件的名字。这些名字不包含路径信息，如果需要得到全路径，需要使用 os.path.join (dirpath, name).


'''


def getdirsize(dir):
    size = 0
    for root, dirs, files in os.walk(dir):
        size += sum([getsize(join(root, name)) for name in files])
    return size


if __name__ == '__main__':
    filesize = getdirsize(r"C:\Users\win\Desktop\2\1")
    print('There are %.3f' % (filesize / 1024 / 1024), 'M bytes in E:\\chengd')
