
a = []
with open(r'F:\123\python-practise\Pyhon100Cases\12.txt', 'r') as fin:
	for i in fin.readlines():
		if '#' in i:
		# if i.find('#') == -1: #这种方法也是可以的
			a.append(i)
		else:
			print(i)
print(a)