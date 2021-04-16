import glob,os

# path='F:\\新建文件夹'
# datafiles =glob.glob(path+'/**/*.txt',recursive=True)  # 递归文件夹下的的所有目录及子目录下的指定类型文件
# print(datafiles)

extensions = ['png', 'jpg', 'jpeg','txt']
file_list = []
dir_name='daisy'
dirpath = 'F: / 新建文件夹'
for extension in extensions:
	file_glob = os.path.join(dirpath,dir_name,'*.' + extension)
	file_list.append(file_glob)
	if not file_list:
		continue
	print('**********************')
	print(file_glob)
	print(file_glob)
print(file_list)