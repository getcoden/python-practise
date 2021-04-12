# conding:utf-8
# author : BJb
# date : 2021/04/12

#遍历法
# 遍历法
# def Traverse(m, n):
#     # 比较大小，并让m为较大值
#     if m < n:
#         m, n = n, m
#     # 遍历最小值n来计算出最大公约数max
#     for i in range(2, n + 1):
#         if (n % i == 0 and m % i == 0):
#             max = i
#     # 计算最小公倍数
#     tiple = m * n
#     a = tiple / max
#     print("遍历法最大公约数  "+str(max))
#     print("遍历法最小公倍数  " + str(a))
	

# 辗转相除法
# def Division_algorithm(m, n):
#     tiple = m * n
#     # 比较大小并求余
#     if m > n:
#         remainder = m % n
#         # 当余数不为零时，赋值求余，当余数为零时，n为最大公约数
#         while (remainder != 0):
#             m = n
#             n = remainder
#             remainder = m % n
#     else:
#         remainder = n % m
#         while (remainder != 0):
#             n = remainder
#             remainder = m % n
#             m = n
#     # 计算最小公倍数
#     min = tiple / n
#     print("辗转相除法最大公约数  "+str(n))
#     print("辗转相除法最小公倍数  "+str(min))

# 更相减损法
def More_loss(m, n):
    i = 0
    tiple = m * n
    # 判断它们是否都是偶数。若是，则用2约简,并记录约简的次数
    while (m % 2 == 0 and n % 2 == 0):
        m = m / 2
        n = n / 2
        i += 1
    # 以较大的数减较小的数，接着把所得的差与较小的数比较，并以大数减小数。直到所得的减数和差相等为止
    if m > n:
        difference = m - n
        while (difference != n):
            m = max(difference, n)
            n = min(difference, n)
            difference = m - n
    else:
        difference = n - m
        while (difference == m):
            n = max(difference, m)
            m = min(difference, m)
            difference = n - m
    # 最大公约数为约掉的若干个2与difference的乘积
    b = difference * i * 2
    # 计算最小公倍数
    a = tiple / b
    print("更相减损法最大公约数  "+str(b))
    print("更相减损法最小公倍数  "+str(a))



if __name__=="__main__":
    # Traverse(m,n)
	m = int(input('m:\n'))
	n = int(input('n:\n'))
	# Division_algorithm(m, n)
	
	More_loss(m,n)
