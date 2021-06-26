import os

# os.path.join() 将分离的部分合成一个整体
filename = os.path.join('/home/ubuntu/python_code', 'split_func')
print(filename)
# 输出为：/home/ubuntu/python_code/split_func

# os.path.splitext()将文件名和扩展名分开
fname, fename = os.path.splitext(
    '/home/ubuntu/python_code/split_func/split_function.py')
print('fname is:', fname)
print('fename is:', fename)
# 输出为：
# fname is:/home/ubuntu/python_code/split_func/split_function
# fename is:.py

# os.path.split（）返回文件的路径和文件名
dirname, filename = os.path.split(
    '/home/ubuntu/python_code/split_func/split_function.py')
print(dirname)
print(filename)
# 输出为：
# /home/ubuntu/python_code/split_func
# split_function.py

# split（）函数
#string.split(str="", num=string.count(str))[n]
# str - - 分隔符，默认为所有的空字符，包括空格、换行(\n)、制表符(\t)等。
# num - - 分割次数。
#[n] - - 选取的第n个分片
string = "hello.world.python"
print(string.split('.'))  # 输出为：['hello', 'world', 'python']
print(string.split('.', 1))  # 输出为：['hello', 'world.python']
print(string.split('.', 1)[0])  # 输出为：hello
print(string.split('.', 1)[1])  # 输出为：world.python
string2 = "hello<python.world>and<c++>end"
print(string2.split("<", 2)[2].split(">")[0])  # 输出为：c++
