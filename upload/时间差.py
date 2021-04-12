#两个日期相隔多少天，例：2008-10-03和2008-10-01是相隔两天 
import datetime
import time

# def datediff(beginDate, endDate):
# 	format = "%Y-%m-%d"
# 	bd = time.strptime(beginDate, format)
# 	ed = time.strptime(endDate, format)
# 	oneday = (ed-bd).days
# 	# count = 0
# 	# while bd != ed:
# 	# 	ed = ed - oneday
# 	# 	count += 1
# 	return oneday

# beginDate = '2011-12-2'
# endDate = '2012-12-2'
# print(datediff(beginDate,endDate))


import sys

def dateinput():
	date = input('please input the first date:')
	return date

def daterans(tdate):
	spdate = tdate.replace('/', '-')
	
	try:
		datesec = time.strptime(spdate,'%Y-%m-%d')
	except ValueError:
		print('%s is not a rightful date!!' % tdate)
		sys.exit(1)
	return time.mktime(datesec)
def daysdiff(d1, d2):
	daysec = 24 * 60 * 60
	return int((d1 - d2) / daysec)
	
date1 = dateinput()
date2 = dateinput()

date1sec = daterans(date1)
date2sec = daterans(date2)
print('The number of days between two dates is: ', daysdiff(date1sec, date2sec))


		