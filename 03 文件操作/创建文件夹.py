import os

# dirpath = r'D:\Premiere\1'
# if not os.path.exists(dirpath):
# 	os.mksdir(dirpath)


# 遍历指定目录，显示目录下的目录和文件名（分开显示）


# def printPath(path):
#     dirList = []
#     fileList = []

#     dirFiles = os.listdir(path)
#     for dirFile in dirFiles:
#         curPath = path + '/' + dirFile
#         if os.path.isdir(curPath):
#             # 排除隐藏文件
#             if dirFile[0] != '.':
#                 dirList.append(curPath)

#         elif os.path.isfile(curPath):
#             if dirFile[0] != '.':
#                 fileList.append(curPath)

#     print('dirlist里有啥？')
#     for dir_ in dirList:
#         print('t', dir_)
#     print('filelist里有啥？')
#     for file_ in fileList:
#         print('t', file_)


# path = r"C:\Users\win\Desktop\ccc"
# printPath(path)


# 遍历指定目录，显示目录下的文件名


# def eachFile(filepath):
#     pathDir = os.listdir(filepath)
#     print('pathDir:', pathDir)
#     for allDir in pathDir:
#         child = os.path.join(filepath, allDir)
#         print(child)


# eachFile(r"C:\Users\win\Desktop\ccc")
