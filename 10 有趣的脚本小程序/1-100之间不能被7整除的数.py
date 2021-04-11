j = 0
for i in range(101):
	if i > 0 and i % 7 == 0:
		continue
	elif i > 0:
		print('{:3d}'.format(i), end=' ')
		j += 1
		if j % 10 == 0:
			print('\n')
			j = 0
	else:
		continue
	