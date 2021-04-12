# f = open('2017级-学生信息-1.txt', 'r')
# while 1:
# 	content = f.readlines()
# 	for i in content:
# 		if (i[0] == '#'):
# 			continue
# 		else:
# 			print(i)
# 	break
# f.close()

# f=open('number.txt','r')
# total=f.read()
# print(total)
# number=[]
# for i in total:
#     number.append(i)
# number.sort()
# print(number)
# f.close()

# import os

# files = os.listdir('./')
# i = 0
# for file in files:
# 	fileFormat = files[i][files[i].find('.'):]
# 	fileName = files[i][:files[i].find('.')]
# 	fileName.strip()
# 	if (fileFormat.strip() == '.txt'.strip()):
# 		os.rename(fileName + fileFormat, "2017-学生信息-" + str(i + 1) + fileFormat)
# 	i = i + 1


import os
folder_path = ('./')
file_list = os.listdir('./')
# 切换到当前文件夹路径下
os.chdir(folder_path)   
for old_name in file_list:
    new_name = "[ZZ出品]" + old_name
    os.rename(old_name, new_name)
    pass