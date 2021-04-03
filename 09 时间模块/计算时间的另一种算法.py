import datetime
import time

# d1 = datetime.datetime(2009, 3, 23)

# d2 = datetime.datetime(2009, 10, 7)

# dayCount = (d1 - d2).days
# print(dayCount)

#-*- encoding:UTF-8 -*-
from datetime import date
import time

nowtime = date.today()
def convertstringtodate(stringtime):
#   "把字符串类型转换为date类型"
	if stringtime[0:2] == "20":
		year=stringtime[0:4]
		month=stringtime[4:6]
		day=stringtime[6:8]
		begintime=date(int(year),int(month),int(day))
		return begintime
	else :
		year="20"+stringtime[0:2]
		month=stringtime[2:4]
		day=stringtime[4:6]
		begintime=date(int(year),int(month),int(day))
		return begintime
def comparetime(nowtime,stringtime):
	"比较两个时间,并返回两个日期之间相差的天数"
	if isinstance(nowtime,date):
	  pass
	else:
	  nowtime=convertstringtodate(nowtime)
	if isinstance(stringtime,date):
	  pass
	else:
	  stringtime=convertstringtodate(stringtime)
	result=nowtime-stringtime
	return result.days

	# if stringtime[0:2] == "20":
	# 	year=stringtime[0:4]
	# 	month=stringtime[4:6]
	# 	day=stringtime[6:8]
	# 	begintime=date(int(year),int(month),int(day))
	# 	endtime=nowtime
	# 	result=endtime-begintime
	# 	return result.days
	# else :
	# 	year="20"+stringtime[0:2]
	# 	month=stringtime[2:4]
	# 	day=stringtime[4:6]
	# 	begintime=date(int(year),int(month),int(day))
	# 	endtime=nowtime
	# 	result=endtime-begintime
	# 	return result.days
a = input('Enter a date(xxxxxx:)')
print (isinstance("20141012",date))
print (comparetime(nowtime,a))

