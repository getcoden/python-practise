'''
在 python 语言中的 random 模块，包含了很多获取随机数或随机字符串的方法，
可以按照指定长度或不定长度获取随机数或字符串。下面利用几个实例说明 random 
模块中的 sample 方法获取随机数字或字符，操作如下：
'''
import random

cu = [2, 3, 4, 7, 6, 1, 9]
print(cu)
hu = random.sample(cu, 4)
print(hu)

ko = ['a', 'g', 'l', 'm', 'e', 'q', 'y', 'u', 'o', 'p']
print(ko)
jw = random.sample(ko, 6)
print(jw)
hw = []
#下面会报错
qt = random.sample(hw, 7)
print(qt)