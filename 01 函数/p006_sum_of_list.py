def sum_of_list(param_list):
	total = 0
	for number in param_list:
		total += number
	return total

list1=[1,2,3,4]		
list2 = [17, 2, 3, 4]
print(f'sum of {list1}',sum_of_list(list1))		
print(f'sum of {list2}',sum_of_list(list2))		
		