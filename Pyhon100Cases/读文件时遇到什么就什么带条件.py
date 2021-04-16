with open('f:/123/python-practise/Pyhon100Cases/1.txt') as lines:
	for line in lines:
		if line.startswith('>>> '):
			expr = line[4:]
			expected = next(lines)
			result = repr(eval(expr, scope))
			if expected != result:
				raise Exception()
print(Exception)