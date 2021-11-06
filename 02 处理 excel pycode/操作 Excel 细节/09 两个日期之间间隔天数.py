import time

start_date = '2017-06-01'
end_date = '2017-06-05'
start_sec = time.mktime(time.strptime(start_date, '%Y-%m-%d'))
end_sec = time.mktime(time.strptime(end_date, '%Y-%m-%d'))
work_days = int((end_sec - start_sec)/(24*60*60))
print(work_days)


