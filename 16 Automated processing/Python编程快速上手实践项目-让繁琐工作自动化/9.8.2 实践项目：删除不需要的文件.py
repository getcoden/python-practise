'''
项目要求：编写一个程序，遍历一个目录树，查找特别大的文件或文件夹， 比方说， 
超过100MB 的文件 （回忆一下，要获得文件的大小，可以使用 os 模块的 os.path.getsize()）。
将这些文件的绝对路径打印到屏幕上。
思路：

这个项目很简单，就是os.path.getsize的运用
1024*1024，这个很小，因为当时我练习时的文件中文件都是几k，按需放大即可
这个只是找出，并没有加入删除的代码
'''


#! python3
# list oversized file in particular folder(and delete it)

import os

for root, dirs, files in os.walk('D:/'):
    for file in files:
        file_name = os.path.join(root, file)
        if os.path.getsize(file_name) > 1024*1024*1024:
            print(file_name)
