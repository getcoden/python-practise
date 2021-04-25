'''
问题描述
　　给定一个长度为 n 的数列，将这个数列按从小到大的顺序排列。1<=n<=200

输入格式
　　第一行为一个整数 n。
　　第二行包含 n 个整数，为待排序的数，每个整数的绝对值小于 10000。
输出格式
　　输出一行，按从小到大的顺序输出排序后的数列。

样例输入
5
8 3 6 4 9
样例输出
3 4 6 8 9
'''

n=int(input('输入一个整数 n:'))
if n>=1 and n<=200:
	s1=list(map(int,input('输入 n 个整数序列:').split()))
	s1.sort()	#默认reverse=False 从小到大输出，reverse=True则相反
	for i in range(len(s1)):
		print(s1[i],end=' ')	#end=' '的作用是输出不换行
