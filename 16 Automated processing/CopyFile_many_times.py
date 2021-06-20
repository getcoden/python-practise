
import os
import shutil
os.chdir('d:\\test')
for x in range(0, 10):  # 需要复制的份数10份
    # 需要另存的位置，名字
    a = 'd:\\test\\' + '00000'+str(x)+'.xls'
# 需要复制的对象

    shutil.copy(r"D:\test\out.xls", a)

'''
import os
import shutil
for x in range(0,10):      #需要复制的份数10份
#需要另存的位置，名字
    a=  '/home/jrx/jiangruixiang/planerecover-masterJRX/nyu/cam/'+'00000'+str(x)+'_cam.txt' 
#需要复制的对象          
    shutil.copy('/home/jrx/jiangruixiang/planerecover-master-JRX/nyu/000005_cam.txt',a)
 
for x in range(10,100):
    a=  '/home/jrx/jiangruixiang/planerecover-master-JRX/nyu/cam/'+'0000'+str(x)+'_cam.txt'
    shutil.copy('/home/jrx/jiangruixiang/planerecover-master-JRX/nyu/000005_cam.txt',a)
 
for x in range(100,1000):
    a=  '/home/jrx/jiangruixiang/planerecover-master-JRX/nyu/cam/'+'000'+str(x)+'_cam.txt'
    shutil.copy('/home/jrx/jiangruixiang/planerecover-master-JRX/nyu/000005_cam.txt',a)
 
for x in range(1000,1449):
    a=  '/home/jrx/jiangruixiang/planerecover-master-JRX/nyu/cam/'+'00'+str(x)+'_cam.txt'
    shutil.copy('/home/jrx/jiangruixiang/planerecover-master-JRX/nyu/000005_cam.txt',a)
'''
