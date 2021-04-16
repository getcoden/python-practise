# def print_str(*str):
# 	return str
# order = print_str('hello', 'world', '!')
# print(order)
# print(type(order))

# def menu(*barbeque):
# 	for i in barbeque:
# 		print('一份烤串:' + i)
		
# menu('烤香肠', '烤肉丸')
# menu('烤鸡翅','烤茄子','烤玉米')

# total = 0
# def sum(arg1, arg2):
# 	total = arg1 + arg2
# 	print('函数内是局部函数:', total)
# 	return total
# sum(10, 20)
# print('函数外是全局变量:', total)

def Math(x):
	y = 5 * x + 3
	print(y)
	# return y
print(Math(4))