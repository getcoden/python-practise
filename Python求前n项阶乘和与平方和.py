factorial = 1
sum1 = 0
n = int(input('输入一个整数，计算阶乘然后求和:'))
str1 = ''
for i in range(1, n + 1):
	for j in range(1, i + 1):
		factorial = factorial * j
	print(str(i) + '!', '=', factorial)
	sum1 = sum1 + factorial
	factorial = 1
	if n != j:
		str1 = str1 + str(j) + '!+'
	else:
		str1 = str1 + str(j) + '!'
print(str1, '=', sum1)
