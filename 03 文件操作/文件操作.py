file1 = open('test.txt', 'r')
list1 = []
while 1:
	line = file1.readline()
	list1.append(line.strip())
	if len(line) == 0:
		break
for l in list1[::-1]:
	print(l)
file1.close()