# -*- coding:utf-8*-
import time
import os
time1 = time.time()
##########################合并同一个文件夹下多个txt################


def MergeTxt(filepath, outfile):
    k = open(filepath+outfile, 'a+')
    for parent, dirnames, filenames in os.walk(filepath):
        for filepath in filenames:
            txtPath = os.path.join(parent, filepath)  # txtpath就是所有文件夹的路径
            f = open(txtPath)
            ##########换行写入##################
            k.write(f.read()+"\n")
    k.close()
    print("finished")


if __name__ == '__main__':
    filepath = r"C:\Users\win\Desktop\cishi"
    outfile = "result.txt"
    MergeTxt(filepath, outfile)
    time2 = time.time()
    print(u'总共耗时：' + str(time2 - time1) + 's')


'''
#coding=utf-8
import os
import os.path #文件夹遍历函数
#获取目标文件夹的路径
filedir = './data/click_data'
#获取当前文件夹中的文件名称列表
filenames=os.listdir(filedir)
#打开当前目录下的result.txt文件，如果没有则创建
f=open('result.txt','w')
#先遍历文件名
for filename in filenames:
    filepath = filedir+'/'+filename
    #遍历单个文件，读取行数
    for line in open(filepath):
        f.writelines(line)
    f.write('\n')
#关闭文件
f.close()
'''

'''
import os

path = "D:\Downloads\网站日志"        # 文件夹目录
files = os.listdir(path)     # 得到文件夹下的所有文件名称
for file in files:  # 遍历文件
    f = open(path+"\\"+file).read()  # 将打开的文件内容保存到变量f
    log = open(path+"\\"+'合成.log', 'a+')  # 以追加模式打开文件
    log.write(f)                     # 写入文件
    print('已经合并：' + file)
'''


'''
 
# -*- coding: utf-8 -*- 

import os,sys 

info = os.getcwd() 
fout = open ('note.tpy', 'w') # 合并内容到该文件 

def writeintofile(info): 
    fin = open(info) 
    strinfo = fin.read() 
    # 利用 ## 作为标签的点缀，你也可以使用其他的 
    fout.write('\n##\n') 
    fout.write('## '+info[-30:].encode('utf-8')) 
    fout.write('\n##\n\n') 
    fout.write(strinfo) 
    fin.close() 


for root, dirs, files in os.walk(info): 
    if len(dirs)==0: 
        for fl in files: 
            info = "%s\%s" % (root,fl) 
            if info [-2:] == 'py': # 只将后缀名为 py 的文件内容合并 
                writeintofile(info) 

    fout.close() 

'''
# 如果你不想合并内容，只想获得一个文件名的清单文件，也可以。
# 这里给你代码。例如，有的作者就会使用这个功能为自己生成一个源代码文件清单，很实用。

'''
 
# -*- coding: utf-8 -*- 
'''
本程序自动搜索指定的目录，
打印所有文件的完整文件名到指定的文件中
''' 
import os,sys 
export = "" 
i=1 
for root, dirs, files in os.walk(r'..'): 
    #r'.' 表示当前目录中的所有清单 
    #.. 表示平行的其他目录，多出很多内容 
    export += "--%s--\n%s\n\n%s\n\n" % (i,root,'\n'.join(files)) 
    i=i+1 
    fp = open('cdcfile-4.txt', 'w') 
    fp.write(export) 
    fp.close() 

'''
