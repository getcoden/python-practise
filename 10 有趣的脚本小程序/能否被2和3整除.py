b=0
while b<5:
	a = int(input('输入一个整数:'))
	if a % 2 == 0 and a % 3 == 0:
		print('该数能被2和3同时整除')
	elif a % 2 == 0:
		print('该数能被2整除')
	elif a % 3 == 0:
		print('该数能被3整除')
	else:
		print('该数不能被2和3同时整除')
	b += 1
	

