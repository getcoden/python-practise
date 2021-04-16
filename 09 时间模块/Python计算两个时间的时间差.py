# coding: utf-8
 
from datetime import datetime
import time
 
format = '%Y-%m-%d %H:%M:%S'
a = datetime.strptime("2019-03-09 08:52:51", format)
b = datetime.strptime("2019-03-09 11:52:51", format)
t1 = time.mktime(a.timetuple()) * 1000 + a.microsecond / 1000
t2 = time.mktime(b.timetuple()) * 1000 + b.microsecond / 1000
a = t2-t1
b = a/1000/3600
c = int(b/24)
d = int(b%24)
print(c)
print(d)

times = "经过了："+str(c)+"天"+str(d)+"小时"
print(times)
print(str(b))