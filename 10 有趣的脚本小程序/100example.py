# peach = 1
# for i in range(9):
# 	peach = (peach + 1) * 2
# print(peach)

# a = 2.0
# b = 1.0
# s = 0
# for n in range(1, 21):
# 	s += a / b
# 	a, b = a + b, a
# print(s)
	
# res = 1
# for i in range(20, 1,-1):
# 	res = i * res + 1
# print(res)

# str = 'love python'
# for i in range(0, len(str)):
# 	letter = str[i]
# 	print(letter,end='')

#斐波那契数列（50位）

# list = []
# for i in range(0, 50):
# 	if i== 0 or i == 1:
# 		list.append(1)
# 	else:
# 		list.append(list[i - 1] + list[i - 2])
# print(list)

# def age(n):
# 	if n == 1:
# 		return 10
# 	return 2 + age(n - 1)
# print(age(5))

# n = int(input('输入一个正整数:'))
# n = str(n)
# print(f'{len(n)}位数')
# print(n[::-1])

# lo = int(input('下限:'))
# hi = int(input('上限:'))
# k = 0

# for i in range(lo, hi + 1):
# 	if i > 1:
# 		for j in range(2, i):
# 			if (i % j) == 0:
# 				break
# 		else:
# 			print(i,end=' ')
# 			k += 1
# print(f'共有{k}个素数')
		
#对10个数进行排序 

# raw = []
# for i in range(10):
# 	x = int(input('int%d: ' % (i)))
# 	raw.append(x)
# for i in range(len(raw)):
# 	for j in range(i, len(raw)):
# 		if raw[i] > raw[j]:
# 			raw[i], raw[j] = raw[j], raw[i]
# print(raw)

# res = 0
# for i in range(1, 101):
# 	if i % 2 != 0:
		
# 		res += i
# print(res)

lis = [1, 10, 100, 1000, 10000, 100000]
n = int(input('insert a number: '))
lis.append(n)
for i in range(len(lis) - 1):
	if lis[i] >= n:
		for j in range(i, len(lis)):
			lis[j], lis[-1] = lis[-1], lis[j]
		break
print(lis)
