
# def bounce(num):
#     height = 100
#     total = 0
#     for i in range(num):
#         total += height
#         height /= 2
#     return total, height
# if __name__ == '__main__':
#     t, h = bounce(10)
#     print(f'它在第10次落地时，共经过{t}米，第10次反弹高度是{h}')



a = [100]  #每个‘反弹落地’过程经过的路程，第1次只有落地（100米）
h = 100  #每个‘反弹落地’过程，反弹的高度，第1次为100米
print('第1次从%s米高落地，走过%s米，之后又反弹至%s米。' % (h, a[0], h/2))
for i in range(2,11):  #第1次已初始化，再循环9次
    a.append(h)  #先计算路程，再高度减半，因为一个‘反弹落地’为2个高度
    h = h / 2
    print('第%s次从%s米高落地，共走过%s米，之后又反弹至%s米。' % (i, h, sum(a), h / 2))



'''
#完整的一个
high = 100
n = 10
high_all = 0 #第n次落地时走过的长度
high_each = 0 #每次落地的高度
def ball_lands(n):
    global high_all, high_each, high
    #小球第一次落地时
    if n == 0:
        high_each = high
        high_all += high_each
        #print('1', high_each, high_all)
        return high_each
    #从小球第n次落地往前推
    high_each = high * (1 / 2) ** n
    print(u'第%d次小球弹起的高度为：%.2f' %(n, high_each))
    high_all += high_each * 2
    #print('2', high_each, high_all)
    ball_lands(n - 1)
 
ball_lands(n)
print(u'小球落地%d次，共经过%.2f米。' % (n,high_all))

'''

# conding:utf-8
# author : BJb
# date : 2021/04/16

# tour = []
# height = []
# hei = 100.0 #起始高度
# tim = 10  #次数

# for i in range(1, tim + 1):
# 	if i == 1:
# 		tour.append(hei)
# 	else:
# 		tour.append(2 * hei)
# 	hei /= 2
# 	height.append(hei)
# print('总高度：tour={0}'.format(sum(tour)))
# print('第10次反弹高度:height={0}'.format(height[-1]))



# high = 200
# total = 100
# for i in range(10):
# 	high /= 2
# 	total += high
# 	print(high / 2)
# print('总长:',total)

h = int(input("请输入起始高度：")) # 获取用户输入
c = int(input("请输入次数："))
tour = [] # 总经过多少米赋值
height = [] # 第n次的高度

for i in range(1,c+1): # 利用for in对次数进行循环，次数的循环改变影响着总体的高度，在这里，对于总里程，我们将球落地时为一个循环
    if i == 1: # 当i为1的时候，将起始高度n添加到tour当中。
        tour.append(h)
    else: # 否则，将 n 循环后高度的一半加入到tour中，因为路程需要经历两次
        tour.append(2*h)
    h /= 2 # 第二次的高度为原始高度的一半
    height.append(h) # 将球每次的高度 加入到height列表当中
s = sum(tour) #对遍历所有i所得到路程结果进行求和
u = height[-1] #最后得到的一个高度

print("%d次经历的总路程为:%f"%(c,s)) # 输出对应的结果 %d,表示整数，%f表示浮点数。
print("第%d次的反弹高度为:%f" % (c, u))


#改造的一个完整的

high = int(input('请输入起始高度:'))
times = int(input('请输入次数:'))
high_all = []
high_each = []
for i in range(1, times + 1):
	if i == 1:
		high_all.append(high)
	else:
		high_all.append(2 * high)
	high /= 2
	high_each.append(high)
	print(f'{i}次经历的总路程为:{high}')
s = sum(high_all)
last_time = high_each[-1]
print(f'{times}次经历的总路程为:{s}')
print(f'第{times}次反弹高度为:{last_time}')
