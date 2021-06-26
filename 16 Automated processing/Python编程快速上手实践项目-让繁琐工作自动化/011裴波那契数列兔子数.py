'''
month = int(input('繁殖几个月?:'))
month_1 = 1
month_2 = 0
month_3 = 0
month_elder = 0
for i in range(month):
	month_1,month_2,month_3,month_elder=month_elder+month_3,month_1,month_2,month_elder+month_3
	print('第%d个月共' % (i + 1), month_1 + month_2 + month_3 + month_elder, '对兔子')
	print('其中1月兔:', month_1)
	print('其中2月兔:', month_2)
	print('其中3月兔:', month_3)
	print('其中成年兔:', month_elder)
'''
# 斐波那契数列的3种计算方式及解析


def fab(n):
    if n == 1:
        return 1
    if n == 2:
        return 1
    if n > 2:
        return fab(n-2)+fab(n-1)


for each in range(1, 11):
    print(fab(each))


def fab2(n):
    a = b = 1
    for each in range(n):
        yield(a)
        a, b = b, a+b


print(list(fab2(10)))


def fab3(n):
    l = [1, 1]
    for x in range(n):
        l.append(sum(l[-2:]))
    return l


print(fab3(10))

# 单单计算前30项，这三种算法就显示出巨大的性能差异，1算法由于含有大量的冗余计算（根本原因是没记性），性能落后2算法1000多倍，而3比2还快6-10倍。

# 生成器法


def fib_yield_for(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
        yield a


for i in fib_yield_for(10):
    print(i, end=' ')
