# a = [1, 3, 6, 4, 5, 7, 2]
# a.sort()
# print(a)

# 降序排列，将reverse参数改为True即可

# a = [1, 3, 6, 4, 5, 7, 2]
# a.sort(reverse=True)
# print(a)

origine = [1, 3, 5, 11, 26, 37, 68, 129]
number = int(input('输入一个数:'))
for i in range(len(origine)):
	if origine[i] <= number and origine[i + 1] >= number:
		origine.append([])
		origine[i+2:len(origine)]=origine[i+1:len(origine)-1]
		origine[i + 1] = number
		break
print(origine)
	