def get_even_number(begin, end):
	result = []
	for item in range(begin, end):
		if item % 2 == 0:
			result.append(item)
	return result

begin = 0
end = 101

print(f'begin={begin},end={end},even numbers:',get_even_number(begin,end))