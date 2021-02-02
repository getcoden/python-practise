# 给定一个数，求数的所有因数

x = int(input("输入数字："))
num = 1
while num <= x:
    if x % num == 0:
        print('因数有:{}'.format(num))
    num = num + 1
