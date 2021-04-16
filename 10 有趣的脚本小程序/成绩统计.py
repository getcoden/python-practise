n = int(input('>>>:'))
num1 = 0
num2 = 0
for _ in range(n):
	score = int(input('>>>:'))
	if score >= 60:
		num1 += 1
	if score >= 85:
		num2 += 1
print(str(round(num1 * 100 / n)) + '%')
print(str(round(num2 * 100 / n)) + '%')


