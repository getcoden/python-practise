while 1:
	try:
		a = input('输入第一个数字,(输入q退出)：')
		if a.lower() == 'q':
			break

		a=int(a)
		
		b = int(input('输入第二个数字：'))
		
		c = a / b
		print(f'结果为:{c}')
	except:
		print('除数不能为0')





