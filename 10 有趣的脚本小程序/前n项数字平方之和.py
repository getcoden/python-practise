
#### 前 n 项数字之和平方

"""
用函数来写
"""

def aSum(n):
	sum = 0
	for i in range(1, n + 1):
		sum += i * i
	return sum

print(aSum(2))


"""
for 循环来写

"""

str1 = ''
sum1 = 0
n = int(input('Type n:'))
total = 0
for i in range(1, n + 1):
	total += i * i 						# total += i **2  也是可以的
	print(str(i)+ '^2', '=', total) 
	sum1 = sum1 + total
	total = 0
	if n != i:
		str1 = str1 + str(i) + '^2+'
	else:
		str1 = str1 + str(i) + '^2'
print(str1, '=', sum1)



"""
平方和与平方和之差

"""
def square_sum_difference(n):
    return int((3 * n ** 2 + 2 * n) * (1 - n ** 2) / 12)
	
print(square_sum_difference(6))


def square_sum_difference(n):
    return int(n * (n + 1) * (2 * n + 1) / 6 - (n * (n + 1) / 2)** 2)
	
print(square_sum_difference(6))



### 前 n 项数字之和平方

def square_sum(numbers):  
    total = 0
    for each in range(1,numbers+1): 
        total = total + each
    return total ** 2

print(square_sum(3))