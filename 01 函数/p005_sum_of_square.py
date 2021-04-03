

def sum_of_square(n):
	result = 0
	for number in range(1, n + 1):
		result += number * number
	return result

# print('sum of square 3:',sum_of_square(3))
# print('sum of square 5:',sum_of_square(5))
# print('sum of square 10:',sum_of_square(10))

while 1:
	in_ = input('请输入一个整数字(输入"q"退出):')
	if in_.lower() == 'q':
		break
	else:
		in_=int(in_)
	print(sum_of_square(in_))