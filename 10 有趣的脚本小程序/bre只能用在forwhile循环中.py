while 1:
	first_number = input('\nFirst number:')
	if first_number.lower() == 'q':
		break

	second_number = input('\nSecond number:')
	try:
		answer = int(first_number) / int(second_number)
	except ZeroDivisionError:
		print("You can't divide by 0!")
	else:
		print(answer)