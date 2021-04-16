import os

# desktop_path = os.path.join(os.path.expanduser('~'), 'Desktop')
# print(desktop_path)



# 写成函数，需要时直接调用更方便


def GetDesktopPath():
    return os.path.join(os.path.expanduser("~"), 'Desktop\\111.txt')   #存放在桌面上的文件在读取时，路径应加 \\ 表示转义

# print(GetDesktopPath())

def Readfiles(b):
	with open(b,encoding='utf-8') as f1:
		for line in f1:		  #用 for 循环一行一行的读取，推荐这读法，不占用内存空间 
			line = line[:-1]  #去除每一行的换行符，即回车产生的空行，使输出时没有空格
			print(line)
	
if __name__ == '__main__':
	a=GetDesktopPath()		#调用函数时，其返回值返回给函数本身，这时用一个变量 ‘a’ 接收，再把 a 传下一个函数使用
	Readfiles(a)		#传实参变量 a 给读取文件的函数 
