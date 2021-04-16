'''
遍历查找文件夹内所有的子文件（不包含文件夹）

用 endswith 判断查找后置是.py 结尾的
'''
# coding:utf-8
import os

def get_files(path='D:\APK\data1', rule=".xlsx"):
    all = []
    for fpathe,dirs,fs in os.walk(path):   # os.walk是获取所有的目录
        for f in fs:
            filename = os.path.join(fpathe,f)
            if filename.endswith(rule):  # 判断是否是"xxx"结尾
                all.append(filename)
    return all

if __name__ == "__main__":
    b = get_files(r"D:\APK\data1")
    for i in b:
        print (i)
