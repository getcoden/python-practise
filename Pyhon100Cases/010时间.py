import time

# for i in range(4):
#     print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))
#     time.sleep(1)

# import time
# for i in range(4):
#     print(str(int(time.time()))[-2:])
#     time.sleep(1)

# def age(n):
# 	if n == 1:
# 		return 10
# 	return 2 + age(n - 1)

# print(age(10))

# def rec(string):
# 	if len(string) != 1:
# 		rec(string[1:])
# 	print(string[0], end='')
# rec(input('string here:'))

# def factorial(n):
# 	return n * factorial(n - 1) if n > 1 else 1
	
# print(factorial(5))

# res = 1
# for i in range(20, 1, -1):
# 	res = i * res + 1
# print(res)

# a = 2.0
# b = 1.0
# s = 0
# for n in range(1, 21):
# 	s += a / b
# 	a, b = a + b, a
# print(s)

# a=set(['x','y','z'])
# b=set(['x','y','z'])
# c=set(['x','y','z'])
# c-=set(('x','z'))
# a-=set('x')
# for i in a:
#     for j in b:
#         for k in c:
#             if len(set((i,j,k)))==3:
#                 print('a:%s,b:%s,c:%s'%(i,j,k))

# peach = 1
# for i in range(9):
# 	peach = (peach + 1) * 2
# print(peach)

# high = 200
# total = 100
# for i in range(10):
# 	high /= 2
# 	total += high
# 	print(high / 2)
# print('总长:',total)

# def factor(num):
#     target=int(num)
#     res=set()
#     for i in range(1,num):
#         if num%i==0:
#             res.add(i)
#             res.add(num/i)
#     return res

# for i in range(2,1001):
#     if i==sum(factor(i))-i:
#         print(i)

a = input('被加数字?:')
n = int(input('加几次?:'))
res = 0
for i in range(n):
	res += int(a)
	a += a[0]
print('结果是:',res)