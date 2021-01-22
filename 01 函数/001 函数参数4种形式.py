1 位置参数


2 关键字参数



3 缺省参数，又叫默认参数

def func(name,age,male = '男'）：
    
    pass


4 不定长参数

（1）多个位置参数列表型参 返回值为元祖形式（）



（2）字典型参  返回值为字典
def myfun(**kwargs):
    print('参数个数:',len(kwargs))
    for k,v in kwargs.items():
        print(k,'->>',v)
    print(kwargs)

myfun(name='midu',age=15,sex='male')