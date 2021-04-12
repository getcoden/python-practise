'''
题目：求三个正整数的最大公约数和最小公倍数。
基本要求：1.程序风格良好(使用自定义注释模板)，两种以上算法解决最大公约数问题，提供友好的输入输出。
提高要求：1.三种以上算法解决两个正整数最大公约数问题。
2.求3个正整数的最大公约数和最小公倍数。
'''
# 求三个正整数的最大公约数和最小公倍数。
a, b, c = map(int, input('请输入三个数: ').split())
# 辗转相除法
# def fun(x, y):
# 	if x < y:
# 		x, y = y, x
# 	d = x % y
# 	while d > 0:
# 		x, y = y, d
# 		d = x % y
# 	return y
# x1 = int(fun(fun(a, b), c))
# x2 = a * b / fun(a, b)
# x2 = int(c * x2 / fun(c, x2))
# print('最大公约数(辗转相除法):', x1)
# print('最小公倍数(辗转相除法):', x2)

# 相除法

# def fun1(x, y):
# 	while x != y:
# 		if x < y:
# 			x, y = y, x
# 		x = x - y
# 	return x

# x1 = int(fun1(fun1(a, b), c))
# x2 = a * b /fun1(a, b)
# x2 = int(c * x2 / fun1(c, x2))
# print('最大公约数(相除法):', x1)
# print('最小公倍数(相除法):', x2)

# 穷举法
def fun2(x, y):
	if x < y:
		x, y = y, x
	for z in range(x, 0, -1):
		if (x % z == 0 and y % z == 0):
			break

	return z

x1 = int(fun2(fun2(a, b), c))
x2 = a * b /fun2(a, b)
x2 = int(c * x2 / fun2(c, x2))
print('最大公约数(穷举法):', x1)
print('最小公倍数(穷举法):', x2)