import random

a = []
while 1:
	if len(a) == 10:
		break
	n = random.randrange(1, 51)
	if n not in a and n % 2 == 0:
		a.append(n)
print(sorted(a))