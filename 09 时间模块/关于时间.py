
from datetime import datetime


# now = datetime.now() # current date and time

# year = now.strftime("%Y")
# print("year:", year)

# month = now.strftime("%m")
# print("month:", month)

# day = now.strftime("%d")
# print("day:", day)

# time = now.strftime("%H:%M:%S")
# print("time:", time)

# date_time = now.strftime("%Y-%m-%d, %H:%M:%S")
# print("date and time:",date_time)
# -----------------------------------------------------------

# today = datetime.now()
# days=int(today.strftime('%j'))
# print(days)
# year_days=365

# str_year = '2021-12-12'
# str_year = datetime.strptime(str_year, '%Y-%m-%d')
# year_ = str_year.year
# b_runnian = False
# if year_ % 100 == 0:
# 	if year_ % 400 == 0:
# 		b_runnian = True
# elif year_ % 4 == 0:
# 	b_runnian = True
# if b_runnian:
# 	year_days=366

# print(year_days)
# year = today.year
# print(year)


out_put_str = '今天是{date_str},{weekday},今年的第{days}天,这一年{pass_ratio}%的时间已流逝'
year_days = 365
today = datetime.now()
date_str = '{year}年{month}月{day}日'.format(year=today.year, month=today.month, day=today.day)
year = today.year
# 判断是否为闰年，闰年条件：能被100整除时，如果可以被400整除，那么是闰年，不能被100整除，能被4整除是闰年
b_runnian = False
if year % 100 == 0:
	if year % 400 == 0:
		b_runnian = True
elif year % 4 == 0:
	b_runnian = True
if b_runnian:
	year_days=366
# 今年的第几天
days = int(today.strftime('%j'))
#数字星期与中文星期的映射关系

week_map = {
	1: '星期一',
	2: '星期二',
	3: '星期三',
	4: '星期四',
	5: '星期五',
	6: '星期六',
	7: '星期日',
}

#星期几
week_day = week_map[today.isoweekday()]
#已过去了多少
pass_ratio = round((days / year_days) * 100, 2)
out_put = out_put_str.format(date_str=date_str, weekday=week_day, days=days, pass_ratio=pass_ratio)

print(out_put)