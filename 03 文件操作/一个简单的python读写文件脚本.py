#! /usr/bin/env python
# author : BJxo
# date : 2021/04/29

import os
import sys
import pandas
from datetime import datetime

# ls = os.linesep

# # get filename
# while True:
#     fname = input('Input an unused file name >')
#     if os.path.exists(fname):
#         print("ERROR:'%s' already exists" % fname)
#     else:
#         break

# # get file content lines
# all = []
# print("\nEnter lines (input '.' to quit).\n")

# # loop until user terminates input
# while True:
#     entry = input('>')
#     if entry == '.':
#         break
#     else:
#         all.append(entry)
# # write lines to file with proper line-ending
# fobj = open(fname, 'w')
# fobj.writelines(('%s%s' % (x, ls) for x in all))
# fobj.close()

# print('done')

# if __name__ == '__main__':
#     print('innter module')

# 下面的代码用来读文件并显示其内容到屏幕上，使用了try-except-else异常处理机制

# get filename
fname=input('Enter filename >')

#attempt to open file for reading
try:
    fobj=open(fname,'r')
except IOError as e:
    print('****** file open error:',e)
else:
    # display contents to the screen
    for eachline in fobj:
        print(eachline)
    fobj.close()
    