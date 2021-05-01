# i = int(input('请输入第一个数:'))
# j = int(input('请输入第一个数:'))
# num_min = min(i, j)
# for n in range(1, num_min + 1):
#     if i % n == 0 and j % n == 0:
#         gys = n
# gbs = (i * j) // gys
# print(f'最大公约数{gys},最小公倍数{gbs}')

'''
nummax, nummin = eval(input("请输入两个正整数，并用逗号连接："))
if (nummax % 1 != 0) or (nummin % 1 != 0):

    print("Error! Please input again:")
    nummax, nummin = eval(input("请输入两个正整数，并用逗号连接："))
if nummax < nummin:
    nummax, nummin = nummin, nummax
gong = set([1])
for i in range(2, nummin+1):
    if (nummax % i == 0) and (nummin % i == 0):
        gong.add(i)
print(str(nummax)+"和"+str(nummin)+"的所有公约数是：", end="")
for j in gong:
    print(j, end=" ")
m = 1
print()
for k in gong:
    if k > m:
        m = k
print("其中最大公约数是："+str(m))
print(str(nummax)+"和"+str(nummin)+"的最小公倍数数是：", end="")
print(int(nummax*nummin/m))
'''
'''
nummax, nummin = eval(input('输入两个数以逗号连接:'))
if (nummax % 1 != 0) or (nummin % 1 != 0):
    print('请输入正确的两个数')
    nummax, nummin = eval(input('请输入两个正整数，并以逗号连接:'))
if nummax < nummin:
    nummax, nummin = nummin, nummax

gong = set([1])
for i in range(1, nummin+1):
    if (nummax % i == 0) and (nummin % i == 0):
        gong.add(i)
print(f'{nummax}和{nummin}的所有公约数是:', end='')
for j in gong:
    print(j, end=' ')

m = 1
print()
for k in gong:
    if k > m:
        m = k
print(f'其中最大公约数是{m},最小公倍数是{int(nummax*nummin/m)}')
'''


# date_str = input('请输入日期,xxxx-xx-xx格式输入:')
# date1_date = datetime.strptime(date_str, '%Y-%m-%d')
# date2_date = datetime.now()
# # date_cha = (date2_date-date1_date).days
# # print(f'\n你今年已经{int(date_cha/365)}岁了。')

# if (date2_date.year % 4 == 0 and date2_date.year % 100 != 0) or (date2_date.year % 400 == 0):
#     print(f'今年是闰年')
# else:
#     print(f'今年是平年')

# a1 = date1_date.strftime('%Y-%m-%d')
# print(a1, type(a1))

# from datetime import datetime
# date_str1 = input('输入第一个日期xxxx-xx-xx:')
# date_str2 = input('输入第二个日期xxxx-xx-xx:')
# date_date1 = datetime.strptime(date_str1, '%Y-%m-%d')
# date_date2 = datetime.strptime(date_str2, '%Y-%m-%d')
# days = 0
# years = 0
# for i in range(date_date1.year, date_date2.year+1):
#     if (i % 4 == 0 and i % 100 != 0) or (i % 400 != 0):
#         years += 1
#     else:
#         years += 1
# print(years)

num = eval(input('请输入数字:'))
print('对应的二进制数:{0:b}\n八进制数：{0:o}\n十六进制数: {0:X}'.format(num))

num1 = int(input('请输入数字:'))
# print(f'对应的二进制数：{bin(num1)},八进制数:{oct(num1)},十六进制数:{hex(num1)}')
print('二进制数是:{0:b}'.format(num1))
print('八进制数是：{0:o}'.format(num1))
print('十六进制数是:{0:x}'.format(num1))
