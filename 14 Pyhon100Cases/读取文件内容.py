li=[]

with open(r'F:\123\python-practise\Pyhon100Cases\number.txt','r') as op:
	for line in op:
		lin = int(line)
		li.append(line.strip())
	print(li)
	lis =  sorted(li)
	print(lis)