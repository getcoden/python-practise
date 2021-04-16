
def data_all():
	'''该函数主要是将所有的.txt文本合并成一个文件
	'''
    f1 = open('./data_all.txt','w',encoding='utf8')
    path = './1/'
    file_name = os.listdir(path)
    # print(file_name)
    for file in file_name:
        with open(path+file,encoding='utf8') as fp:
            for line in fp.readlines():
                line = line.strip()
                if line == '':
                    continue
                f1.write(line+'\n')
    f1.close()
data_all()
