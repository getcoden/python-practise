
# m = m1 = eval(input('请输入第一个正整数:'))
# n = n1 = eval(input('请输入第一个正整数:'))
# if m1 >= n1:
# 	while n1 != 0:
# 		a = m1 % n1
# 		m1 = n1
# 		n1 = a
# 	u = (m * n) // m1
# 	print(f'最大公约数{m1},最小公倍数{u}')
# else:
# 	while m1 != 0:
# 		a = n1 % m1
# 		n1 = m1
# 		m1 = a
# 	u = (m * n) // n1
# 	print(f'最大公约数{n1},最小公倍数{u}')

# m = int(input('请输入m的值:'))
# n = int(input('请输入n的值:'))

# if m < n:
# 	t = m
# 	m = n
# 	n = t
	
# if (m % n == 0):
# 	x = n
# 	y = m
	
# else:
# 	for i in range(1, n):
# 		if m % i == 0 and n % i == 0:
# 			x = i
# 		y = m
# 		while 1:
# 			if y % m == y % n == 0:
# 				break
# 			y += 1
# print(f'最大小公约数为:{int(x)},最小公倍数为:{int(y)}')

# 函数来写求最大公约数和最小公倍数

# def main():
# 	x = int(input('x= '))
# 	y = int(input('y= '))
# 	if x > y:
# 		(x, y) = (y, x)
# 	for factor in range(x, 0, -1):
# 		if x % factor == 0 and y % factor == 0:
# 			print(f'{x}和{y}的最大公约数是{factor}')
# 			print(f'{x}和{y}的最小公倍数是{x*y//factor}')
# 			break

# if __name__ == '__main__':
# 	main()

# i = int(input('请输入第一个数:'))
# j = int(input('请输入第一个数:'))
# num_min = min(i, j)
# for n in range(1, num_min + 1):
# 	if i % n == 0 and j % n == 0:
# 		gys = n
# gbs = (i * j) // gys
# print(f'最大公约数{gys},最小公倍数{gbs}')

# nummax,nummin=eval(input("请输入两个正整数，并用逗号连接："))
# if (nummax % 1 != 0) or (nummin % 1 != 0) :
#     print("Error! Please input again:")
#     nummax,nummin=eval(input("请输入两个正整数，并用逗号连接："))
# if nummax < nummin :
#     nummax,nummin=nummin,nummax
# gong=set([1])
# for i in range(2,nummin+1):
#     if (nummax % i ==0) and (nummin % i ==0):
#         gong.add(i)
# print(str(nummax)+"和"+str(nummin)+"的所有公约数是：",end="")
# for j in gong:
#     print(j,end=" ")
# m=1
# print()
# for k in gong:
#     if k>m :
#         m=k
# print("其中最大公约数是："+str(m))
# print(str(nummax)+"和"+str(nummin)+"的最小公倍数数是：",end="")
# print(int(nummax*nummin/m))

# conding:utf-8
# author : BJb
# date : 2021/04/08

#求2个整数的最大公约数和最小公倍数，Python解法

# def gdc(p, q):
# 	'''求整数p,q的最大小公约数
# 	'''
# 	if q == 0:
# 		return p
# 	if p < q:
# 		p, q = q, p
# 	r = p % q
# 	return gdc(q, r)
	
# def mdc(p, q):
# 	'''求最小公倍数，先求最大公约数，最小公倍数=他们的乘积/最大公约数
# 	'''
# 	gd = gdc(q, q)
# 	return p * q // gd
# if __name__ == '__main__':
# 	p = 12
# 	q = 15
# 	print('两个整数:%d,%d' % (p, q))
# 	print(f'最大公约数:{gdc(p,q)}' )
# 	print(f'最小公倍数{mdc(p, q)}')
	
# def hcf(u, v):
# 	"""该函数返回两个数的最大公约数"""

# # 交换u,v,保证u>v
# 	if v > u:
# 		u, v = v, u
# 		t = u % v
# 		while (t != 0):
# 			u, v, t = v, t, u % v
# 	return v

# def lcd(u, v):
# 	"""该函数返回两个数的最小公倍数"""
# 	return u*v//hcf(u,v)

# num1 = int(input('请输入第一个数字:'))
# num2 = int(input('请输入第二个数字:'))
# print(f'最大公约数{hcf(num1,num2)}')
# print(f'最小公倍数{lcd(num1,num2)}')

#获取两个整数，求这两个整数的最大公约数和最小公倍数。最大公约数计算一般使用辗转相除法，最小公倍数计算则使用两个数##的乘积除以最小公倍数。

# s1 = int(input('num1:'))
# s2 = int(input('num2:'))
# a = s1
# b = s2
# c = 0
# s = a * b
# if a < b:
# 	a, b = b, a
# while a % b != 0:
# 	c = a % b
# 	a = b
# 	b = c
# var1 = s // b
# print(f'{s1}和{s2}的最小大公数是{b}，最小公倍数是{var1}')


# -*- coding: utf-8 -*-

#定义求公约数的方法
'''
本题要求两个给定正整数的最大公约数和最小公倍数。

输入格式:

输入在一行中给出两个正整数m和n(≤1000)。

输出格式:

在一行中顺序输出m和n的最大公约数和最小公倍数，两数字间以1空格分隔。

代码如下：
'''

def gys(a,b):

	if a%b == 0:

		return b

	else:

		return gys(b,a%b)

s = input().split()

a = int(s[0])

b = int(s[1])

print("{:d} {:d}".format((gys(a,b)),a*b//(gys(a,b))))

'''
这个程序简单，主要是知道公约数和公倍数怎么得到。

最小公倍数：

最小公倍数=两个证书的乘积除以最大公约数。

最大公约数：

有整数a b

1.如果a%b 取余等于0，则b就是最大公约数。

2.如果不等于0，那么就让a=b，b=余数，再去做取余。

3.余数为0时，那个b就是最大公约数。
'''