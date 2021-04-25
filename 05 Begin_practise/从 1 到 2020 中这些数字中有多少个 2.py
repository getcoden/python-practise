'''
ans=0
for i in range(1,2021):
	ans+=(str(i).count('2'))
print(f'共有{ans}个2')
'''

'''
第三题。跑步
原问题：小明坚持每天跑步，正常情况下每天跑一公里，如果这一天是周一或者月初（每月的一号），那么小明就会跑两公里（如果这一天既是周一，又是月初，小明也是跑两公里），小明从 2000 年 1 月 1 日（周六）一直坚持到了 2020 年 10 月 1 日（周四），请你计算一下小明共跑了多少公里？

解题思路：就是统计 2000 年 1 月 1 日到 2020 年 10 月 1 日（包含）以来共有多少天是周一或者月初，考试的时候绞尽脑汁写得代码，结果还错了，事后看别人题解才知道还有 datetime 库这个东西，我哭了。
'''

# from datetime import *

# start=date(2000,1,1)
# end=date(2020,10,2)
# tmp=timedelta(days=1)
# ans=0
# while start !=end:
# 	if start.weekday()==0 or start.day==1:
# 		ans+=2
# 	else:
# 		ans+=1
# 	start=start+tmp
# print(f'小明共跑了{ans}公里。')

# sum=0
# s=0
# while s<=100:
# 	if s%2==0:
# 		sum+=s
# 	s+=2
# print(f'1到100之间的偶数和是{sum}')
