"""题目
已知任意两个日期，计算出两个日期之间相隔的天数。

实现思路1
这里我们运用 Python 里面内置模块 time 来处理问题。

已知2个日期，格式为 yyyy-mm-dd
通过 time.strptime() 方法，把日期时间字符串解析为时间元组
通过 time.mktime() 方法，把时间元祖转换为时间戳
根据2个日期对应的时间戳，得到2个日期相差的秒数，进而计算出间隔天数
代码实现
"""
import time


# def demo(day1, day2):
#     time_array1 = time.strptime(day1, '%Y-%m-%d')
#     timestamp_day1 = int(time.mktime(time_array1))
#     time_array2 = time.strptime(day2, '%Y-%m-%d')
#     timestamp_day2 = int(time.mktime(time_array2))
#     result = (timestamp_day2-timestamp_day1)//60//60//24
#     return result


# day1 = '2018-07-09'
# day2 = '2020-09-26'

# day_diff = demo(day1, day2)
# print(f'两个日期的间隔天数:{day_diff}')


"""
实现思路2
这里我们不使用 时间函数 来处理问题，我们可以先计算出每个日期距离公元元年1月1日的总天数，再求出两个日期的间隔天数。

需要判断某个年份是不是闰年，如果是闰年，则该年份天数为365+1
通过一个列表来存储每月份的天数，如果所给的2个日期中，年份是闰年，则2月份天数为28+1
根据所给的日期，遍历年月日，分别计算出2个日期距离公元元年1月1日的总天数
两个总天数相减，即可求出两个日期之间的天数
注意：

闰年的计算方法是 "四年一闰，百年不闰，四百年再闰" ，也就是说一般有以下两个条件：

能被4整除且不能被100整除的是闰年
能被400整除的是闰年
代码实现
"""

'''
def is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        return 1
    else:
        return 0


def get_days(year, month, day):
    days = 0
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if is_leap_year(year):
        month_days[1] = 29
    for i in range(1, year):
        year_day = 365
        if is_leap_year(i):
            year_day = 366
        days += year_day
    for m in range(month - 1):
        days += month_days[m]
    days += day
    return days


def get_result(start_time, end_time):
    res = end_time - start_time
    return res


year1, month1, day1 = 2018, 7, 9
year2, month2, day2 = 2020, 9, 26
days1 = get_days(year1, month1, day1)
days2 = get_days(year2, month2, day2)
day_diff = get_result(days1, days2)

print("两个日期的间隔天数：{} ".format(day_diff))
'''

# 好的命名方法


start_time = '2019-06-01'
end_time = '2019-09-18'
start = time.mktime(time.strptime(start_time, '%Y-%m-%d'))
end = time.mktime(time.strptime(end_time, '%Y-%m-%d'))
count_days = int((end-start)/(24*60*60))
print(count_days)


# 两个日期间的天数统计

# 使用split函数将输入的日期字符串格式化成字符列表
t1 = input('日期一: ').split('/')
t2 = input('日期二: ').split('/')
print('t1:', t1)
print('t2:', t2)

# 按照struct_time类型中元素构建元组用于计算时间戳
time1 = (int(t1[0]), int(t1[1]), int(t1[2]), 0, 0, 0, 0, 0, 0)
time2 = (int(t2[0]), int(t2[1]), int(t2[2]), 0, 0, 0, 0, 0, 0)
print('time1:', time1)
print('time2:', time2)

# 使用time_mktime()分别计算两个日期时间戳
timestru1 = time.mktime(time1)
timestru2 = time.mktime(time2)
print('timestru1日间戳: ', timestru1)
print('timestru2日间戳: ', timestru2)
print(f'两个日期 之间的总天数为:{int(abs(timestru2-timestru1))//24//3600}')

