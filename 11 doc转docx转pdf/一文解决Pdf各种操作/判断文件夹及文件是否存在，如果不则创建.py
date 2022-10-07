import os


def batch_create_files(filepath):
    fd = os.path.exists(filepath)
    if not fd:
        try:
            fo = open(filepath, mode='x')
            print(filepath + '创建成功')
            fo.close()
        except IOError:
            print('创建失败')


batch_create_files('C:\\Users\\win\\Desktop\\2_txt.txt')


# try:
#     f = open("D:/1.txt", 'r')
#     f.close()
# except IOError:
#     f = open("D:/1.txt", 'w')
