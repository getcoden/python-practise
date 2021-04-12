import math

count = 0

for i in range(100, 200):
	for j in range(2, round(math.sqrt(i)) + 1):
		if i % j == 0:
			break
	else:
		print(i, end=' ')
		count += 1
print(f'\n一共有{count}个')

		