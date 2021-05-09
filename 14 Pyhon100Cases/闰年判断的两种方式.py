'''
首先明确  什么是闰年？

1、能被 4 整除，但不能被 100 整除；

2、能被 400 整除；
'''
# 方案1
'''
while True:
    year = input('请输入要判断的年份(例如：2000):')
    if year.isdigit():
        year = int(year)
        result = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
        if result:
            s = '是闰年'
        else:
            s = '不是闰年'
        print(f'{year}年{s}')
    else:
        print('请输入年份！')
'''

# 方案2
while True:
    year = input("请输入您要判断的年份（例如：2000）：")
    if year.isdigit():
        yea = int(year)
        if (yea/400 == int(yea/400)) or ((yea/4 == int(yea/4)) and (yea/100 != int(yea/100))):
            print(year+"是闰年！")
        else:
            print(year+"不是闰年！")
    else:
        print("请输入年份！")
