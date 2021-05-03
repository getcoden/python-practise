
# -*- coding: UTF-8 -*-

from tqdm import trange
from time import sleep


'''
import sys, time

class ShowProcess():
    """
    显示处理进度的类
    调用该类相关函数即可实现处理进度的显示
    """
    i = 0 # 当前的处理进度
    max_steps = 0 # 总共需要处理的次数
    max_arrow = 50 #进度条的长度
    infoDone = 'done'

    # 初始化函数，需要知道总共的处理次数
    def __init__(self, max_steps, infoDone = 'Done'):
        self.max_steps = max_steps
        self.i = 0
        self.infoDone = infoDone

    # 显示函数，根据当前的处理进度i显示进度
    # 效果为[>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>]100.00%
    def show_process(self, i=None):
        if i is not None:
            self.i = i
        else:
            self.i += 1
        num_arrow = int(self.i * self.max_arrow / self.max_steps) #计算显示多少个'>'
        num_line = self.max_arrow - num_arrow #计算显示多少个'-'
        percent = self.i * 100.0 / self.max_steps #计算完成进度，格式为xx.xx%
        process_bar = '[' + '>' * num_arrow + '-' * num_line + ']'\
                      + '%.2f' % percent + '%' + '\r' #带输出的字符串，'\r'表示不换行回到最左边
        sys.stdout.write(process_bar) #这两句打印字符到终端
        sys.stdout.flush()
        if self.i >= self.max_steps:
            self.close()

    def close(self):
        print('')
        print(self.infoDone)
        self.i = 0
def do_something():
    s=0
    for i in range(100):
        s += i
    return s

if __name__=='__main__':
    max_steps = 100
    
    process_bar = ShowProcess(max_steps, 'OK')
    
    for i in range(max_steps):
        
        process_bar.show_process()
        do_something()
        time.sleep(0.01)

'''

#号进度条
'''
import time
 
 
class Index(object):
    def __init__(self, number=50, decimal=2):
        """
        :param decimal: 你保留的保留小数位
        :param number: # 号的 个数
        """
        self.decimal = decimal
        self.number = number
        self.a = 100/number   # 在百分比 为几时增加一个 # 号
 
    def __call__(self, now, total):
        # 1. 获取当前的百分比数
        percentage = self.percentage_number(now, total)
 
        # 2. 根据 现在百分比计算
        well_num = int(percentage / self.a)
        # print("well_num: ", well_num, percentage)
 
        # 3. 打印字符进度条
        progress_bar_num = self.progress_bar(well_num)
 
        # 4. 完成的进度条
        result = "\r%s %s" % (progress_bar_num, percentage)
        return result
 
    def percentage_number(self, now, total):
        """
        计算百分比
        :param now:  现在的数
        :param total:  总数
        :return: 百分
        """
        return round(now / total * 100, self.decimal)
 
    def progress_bar(self, num):
        """
        显示进度条位置
        :param num:  拼接的  “#” 号的
        :return: 返回的结果当前的进度条
        """
        # 1. "#" 号个数
        well_num = "#" * num
 
        # 2. 空格的个数
        space_num = " " * (self.number - num)
 
        return '[%s%s]' % (well_num, space_num)
 
 
 
index = Index()
 
start = 371
for i in range(start + 1):
    print(index(i, start), end='')
    time.sleep(0.01)
    # \r 返回本行开头
    # end : python 结尾不加任何操作, 默认是空格
'''

import sys, time
 
# print("正在下载......")
# for i in range(11):
#     if i != 10:
#         sys.stdout.write("==")
#     else:
#         sys.stdout.write("== " + str(i*10)+"%/100%")
#     sys.stdout.flush()
#     time.sleep(0.2)
# print("\n" + "下载完成")




# import time
# print("程序启动中,请稍等:")
# for i in range(26):
#     a = "■" * i
#     b = "□" * (25 - i)
#     c = (i / 25) * 25 * 4
#     print("\r{}{}{:.2f}%".format(a, b, c), end="")
#     time.sleep(0.1)

import sys
import time

def progressbar(it, prefix="", size=60, file=sys.stdout):
    count = len(it)
    def show(j):
        x = int(size*j/count)
        file.write("%s[%s%s] %i/%i\r" % (prefix, "#"*x, "."*(size-x), j, count))
        file.flush()        
    show(0)
    for i, item in enumerate(it):
        yield item
        show(i+1)
    file.write("\n")
    file.flush()

def do_something():
    s=0
    for i in range(100):
        s += i
    return s
    
for i in progressbar(range(100), "Computing: ", 40):
    do_something()
    time.sleep(0.1)
	
