account = 'wang'
password = '123456'
money = 10000
userAccount = input('请输入账号:')
userPsw = input('请输入密码:')
if account == userAccount and password == userPsw:
	userMoney = int(input('请输入取款金额:'))
	if userMoney <= money:
		money -= userMoney
		print('您取现%d元,余额%d元' % (userMoney, money))
	else:
		print('余额不足')
else:
	print('账号或密码错误')