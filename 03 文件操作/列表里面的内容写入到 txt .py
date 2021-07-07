'''
方法一
将列表写入 txt 文件中
如下代码所示
a 是一段二维列表，需要把它写入一个 txt 文件中，
'''

# a = [['1', '9'], ['2', '5'], ['3', '3'], [
#     '2', '4'], ['4', '3'], ['1', '8'], ['1', '9']]

# t = ''
# with open(r'D:\test1\N_a.txt', 'w') as q:
#     for i in a:
#         for e in range(len(a[0])):
#             t = t + str(i[e]) + ' '
#         q.write(t.strip(' '))
#         q.write('\n')
#         t = ''

'''
u = [['mov', 'push', 'push', 'call', 'push', 'push', 'push', 'call'], ['pop', 'push', 'call', 'pop', 'retn', 'mov', 'push', 'call', 'push'], [
    'push', 'push', 'call', 'pop', 'call', 'pop', 'retn', 'mov', 'push'], ['lea', 'push', 'call', 'test', 'jnz', 'push', 'push']]
t = ''
with open(r'd:\test1\1.txt', 'w+') as q:
    for i in u:
        for e in range(len(i)):
            t = t + str(i[e]) + ' '
        q.write(t.strip(' '))
        q.write('\n')
        t = ''
'''

# 方法二

# 在已有内容的 txt 文件的后面，再存入新的内容
# 只需将之间的打开方式由 file = open(filename, 'w') 改为 file = open(filename, 'a') 即可。

'''
sPath = r'd:\test1'
os.chdir(sPath)
u = [['mov', 'push', 'push', 'call', 'push', 'push', 'push', 'call'], ['pop', 'push', 'call', 'pop', 'retn', 'mov', 'push', 'call', 'push'], [
    'push', 'push', 'call', 'pop', 'call', 'pop', 'retn', 'mov', 'push'], ['lea', 'push', 'call', 'test', 'jnz', 'push', 'push']]


def text_save(filename, data):  # filename为写入txt文件的路径，data为要写入数据列表.
    file = open(filename, 'a')
    for i in range(len(data)):
        s = str(data[i]).replace(
            '[', '').replace(']', '')  # 去除[],这两行按数据不同，可以选择
        s = s.replace("'", '').replace(',', '') + '\n'  # 去除单引号，逗号，每行末尾追加换行符
        file.write(s)
    file.close()
    print('保存文件成功')


ops = [['i', 'love', 'china'], ['happy', 'birthday']]
text_save('./N_aa.txt', ops)
os.system('explorer.exe ' + sPath)
'''
# Python：将 list 写入一个 txt 文件四种方法
import re
import os
path = r'd:\test1'
os.chdir(path)

a = [
    {"Jodie1": "123"},
    {"Jodie2": "456"},
    {"Jodie3": "789"},
]

# 方法一

# with open(r'./1.txt', 'a') as f:
#     for i in range(len(a)):
#         for key, values in a[i].items():
#             print(key + "," + values + "\r")
#             f.write(key + "," + values + '\r')

# 方法二

file = open('./1.txt', 'a')
for i in range(len(a)):
    s = str(a[i]).replace('{', '').replace('}', '').replace(
        "'", '').replace(':', ',') + '\n'
    file.write(s)
file.close()

# 方法三

# import re
# file3 = open('./1.txt', 'a')
# for i in range(len(a)):
#     s = (re.sub(r"['{ },]*", '', str(a[i])) + '\n').replace(':', ',')
#     file3.write(s)
# file3.close()

# 方法四

with open('./1.txt', 'a') as f:
    for i in range(len(a)):
        s = (re.sub(r"[{ },]*", '', str(a[i])) + '\n').replace(':', ',')
        f.write(s)
