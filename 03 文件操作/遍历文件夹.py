import os

path=r'D:\Premiere'
for dirpath, dirnames, filenames in os.walk(path):
	print(f'打开文件夹{dirpath}')
	if dirnames:
		print(dirnames)
	if filenames:
		print(filenames)
	print('-' * 10)
	