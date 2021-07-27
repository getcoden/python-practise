
import os  # 导入库
import sys
import random
import os
'''
import os

def mkdir(path):

    folder = os.path.exists(path)

    if not folder:  # 判断是否存在文件夹如果不存在则创建为文件夹
        os.makedirs(path)  # makedirs 创建文件时如果路径不存在会创建这个路径
        print("---  new folder...  ---")
        print("---  OK  ---")

    else:
        print("---  There is this folder!  ---")


file = "D:\\xxoo\\test"
mkdir(file)  # 调用函数
'''
# os.getcwd() 可以查看 py 文件所在路径；

# 在 os.getcwd() 后边 加上[:-4] + 'xxoo\\' 就可以在 py 文件所在路径下创建 xxoo 文件夹
'''
import os

folder = os.getcwd()[:-4] + 'new_folder\\test\\'
# 获取此py文件路径，在此路径选创建在new_folder文件夹中的test文件夹

if not os.path.exists(folder):
    os.makedirs(folder)
print(folder)
'''

# 创建 txt 文件

# 在桌面创建一个名字为 new 的 txt 文件

# file = open('C:\\Users\\win\\Desktop\\' + 'new' + '.txt', 'w')
# file.close()

# 在 py 文件路径下创建 test 的 txt 文件

'''
def txt(name, text):  # 定义函数名
    b = os.getcwd()[:-4] + 'new\\'

    if not os.path.exists(b):  # 判断当前路径是否存在，没有则创建new文件夹
        os.makedirs(b)

        xxoo = b + name + '.txt'  # 在当前py文件所在路径下的new文件中创建txt

    file = open(xxoo, 'w')

    file.write(text)  # 写入内容信息

    file.close()
    print('ok')


txt('test', 'hello,python')  # 创建名称为test的txt文件，内容为hello,python
'''

# 代码中创建文件夹
# sentence = "You are a beautiful girl, I love you, I know you will be different six months later, enjoy the good time of the six months."
# sentence = sentence.split()
# print(sentence)


# def CreatDir():
#     index = 0
#     for sub in sentence:
#         path = "c:/Users/win/Desktop/SceretPaper/" + sub + str(index)
#         os.makedirs(path)
#         index += 1
# CreatDir()
'''
def mkdir(path):
    # function：新建文件夹
    # path：str-从程序文件夹要要创建的目录路径（包含新建文件夹名）
    # 去除首尾空格
    path = path.strip()  # strip方法只要含有该字符就会去除
    # 去除首尾\符号
    path = path.rstrip('\\')
    # 判断路径是否存在
    isExists = os.path.exists(path)

    # 根据需要是否显示当前程序运行文件夹
    # print("当前程序所在位置为："+os.getcwd())

    if not isExists:
        os.makedirs(path)
        print(path+' 创建成功')
        return True
    else:
        print(path+'目录已存在')
        return False


mkdir('C://Users//win//Desktop//1')
'''

'''
# 用于创建一个在当前程序目录下的文件夹
path_file = os.path.abspath(os.path.dirname(sys.argv[0]))
path_file = path_file+'/data'  # make a dir called data

try:
    os.makedirs(path_file)
except:
    print('path has been builded')
'''

'''
path = './test_data/test_data1/'		# 想要创建的文件

# if os.path.isdir(path) == False:  # 如果 test_data1 该文件不存在，就创建该文件
#     os.mkdir(path)  # 前提是 test_data 这个路径是存在的

#  如果想要递归创建文件，则使用
if os.path.isdir(path) == False:
    # 如果 test_data 不存在，就递归地创建，即先创建 test_data 文件夹， 再创建 test_data1 文件夹
    os.makedirs(path)
'''
# base_dir = os.path.dirname(__file__)
# print(base_dir)

# base_dir = os.getcwd()
# print(base_dir)
