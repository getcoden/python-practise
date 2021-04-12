# try:
# 	f = open('testfile.txt', 'w')
# 	f.write('这是一个测试文件，用于测试异常！！')
# except IOError:
# 	print('Error：没有找到文件或读取文件失败')
# else:
# 	print('内容写入文件成功')
# 	f.close()


### 在执行代码前为了测试方便，我们可以先去掉 testfile 文件的写权限，命令如下：

# try:
# 	f = open('testfile.txt')
# 	f.write('这是一个测试文件，用于测试异常！！')
# except IOError:
# 	print('Error：没有找到文件或读取文件失败')
# else:
# 	print('内容写入文件成功')
# 	f.close()

# def div(a, b):                  # 定义一个除法函数
# 	try:                        # 正常分支
# 		c = a / b          
# 		return c
# 	except ZeroDivisionError as ex_obj:
# 		print("Got Exception: %s" % ex_obj)
# 	finally:
# 		print(u"finnally分支在执行")
# 					# 函数定义结束

# div(2,0)

def finally_demo(a, b):            # 定义一个包含异常处理的函数
	try:
	    a = a / b
	except ZeroDivisionError as except_obj:   # 捕捉被0除的异常
	    print("Exception Message = %s" % except_obj)
	else:                          # 没有异常时会触发的分支
	    print("No Exception is Got")
	finally:                       # 不论有无异常都被触发的分支
	    print("Finnally Branch is Running")

finally_demo(12, 2)