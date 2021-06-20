'''
 工作习惯问题，经常将每日工作建立一个文件夹，
 并把当天的工作内容存放到一个规范命名（通常就是一个日期名字）的文件夹内，
 直到有一天突然需要将所有文件合并到一个文件夹下面压缩发送给领导的时候，懵逼了，
 要一个个文件夹打开，并粘贴到一个汇总的文件夹下面么？。。。。。
'''
import os
import shutil

# to generate a file, and make sure the file has not existed
try:
    os.makedirs("D:\数据汇总0")
except FileExistsError:
    pass


def Move1(dir):
    i = 0
    for root, dir1, filename in os.walk(dir):
        for index in range(len(filename)):
            # 这里注意 filename 是个元组，splitext 方法的时候只能是字符串
            if os.path.splitext(filename[index])[1] == '.xls':
                i += 1
                root1 = "D:\数据汇总0"
                old_path = os.path.join(root, filename[index])
                new_path = os.path.join(root1, filename[index])
                shutil.copyfile(old_path, new_path)
    print("总共有", i, "图层文件被复制!")


Move1(r"D:\test\excel")
