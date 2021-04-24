num8 = input("请输入:")
for i in range(len(num8)):
	if ord(num8[i]) >= 97 and ord(num8[i]) <= 122:
		print(chr(ord(num8[i]) - 32),end = "")
	elif ord(num8[i]) >= 65 and ord(num8[i]) <= 90:
		print(chr(ord(num8[i]) + 32),end = "")
	else:
		print(num8[i],end ="")