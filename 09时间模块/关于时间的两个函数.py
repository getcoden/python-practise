from datetime import datetime
import time
start_str='2001-02-03'
 
start_date = datetime.strptime(start_str, '%Y-%m-%d')
str_date = start_date.strftime('%Y-%m-%d')

print(start_date)
print(str_date)

print(type(start_date))