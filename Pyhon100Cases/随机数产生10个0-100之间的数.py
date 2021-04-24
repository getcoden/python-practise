import random

i = 0
f = open(r'F:\123\python-practise\Pyhon100Cases\number.txt', 'w+')
while i < 10:
	y = int(random.random() * 100)
	print(y)
	f.write(str(y) + '\n')
	f.flush()
	i = i + 1
	