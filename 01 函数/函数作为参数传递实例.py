# def get_nums(*nums):
# 	res=0
# 	print(nums)
# 	for i in nums:
# 		res+=i
# 	print(res)
	
# l=[1,2,3]
# get_nums(*l)

# print('-'*40)
# def get_vk(**kwargs):
# 	for k,v in kwargs.items():
# 		print('k/v:{0}==>{1}'.format(k,v))

# dicta={'name':'test','age':24,'email':'test@qq.com'}
# get_vk(**dicta)

def numbers():
	listt=list(map(int,input().split(' ')))
	return listt

# listt=list(map(int,input().split(' ')))
# li=numbers(listt)
# print(type(li))
# print(li)

def get_max(nums):
	m=max(nums)
	mi=min(nums)
	avg=sum(nums)/len(nums)
	print(f'最大:{m},最小{mi},{avg}')
	print(type(len(nums)))

get_max(numbers())









