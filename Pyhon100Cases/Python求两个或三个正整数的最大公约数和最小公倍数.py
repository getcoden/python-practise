# 辗转相除法求最大公约数
#
# a = int(input("请输入a的值:"))
# b = int(input("请输入b的值:"))
# c = 0
# if a<b:
#     c = a
#     a = b
#     b = c
# while a%b!=0:
#     c = a%b
#     a = b
#     b = c
# print("最大公约数为:" +str(b))






# 相减法求最大公约数


# a = int(input("请输入a的值:"))
# b = int(input("请输入b的值:"))
# c = 0
# if a<b:
#     c = a
#     a = b
#     b = c
# while a-b!=0:
#     c = a-b
#     a = b
#     b = c
# print("最大公约数为:" +str(b))





#第三个方法求最大公约数

#输入两个数字，循环出1到两个数最小值之间的数，当这个数同时能够被a和b整除时，将这些数保存在数组i[]中
#使用sort()对数组i进行从小到大的排序，使用i[-1]，输出数组i[]的最大值，即最大公约数

# a = int(input("请输入a的值:"))
# b = int(input("请输入b的值:"))
# if a>b:
#     t = a
#     a = b
#     b = t
# for n in range(1,a+1):
#     if a%n==0 and b%n==0:
#         i = [n]
#         i.sort()
# print("最大公约数为:" + str(i[-1]))
#
#
#
#
#



#求三个数的最大公约数：先求出两个数的最大公约数，再求它与另一个数的最大公约数
# a = int(input("请输入a的值:"))
# b = int(input("请输入b的值:"))
# c = int(input("请输入c的值:"))
# if a>b:
#     t = a
#     a = b
#     b = t
# for n in range(1,a+1):
#     if a%n==0 and b%n==0:
#         i = [n]
#         i.sort()
# m = i[-1]
# print("a和b的最大公约数为:" + str(m))
# if m>c:
#     l = m
#     m = c
#     c = l
# for n in range(1, m+1):
#     if m%n == 0 and c%n == 0:
#         p = [n]
#         p.sort()
# print("a b c的最大公约数为:" + str(p[-1]))
#
#



# 第一种求最小公倍数的方法
# 求三个数的最小公倍数，分别循环出三个数的倍数，在找出相同的数，放在数组中，输出最小值即可
# a = int(input("请输入a的值:"))
# b = int(input("请输入b的值:"))
# c = int(input("请输入c的值:"))
# d = a * b * c
# m = []
# n = []
# o = []
# for i in range(1, d + 1):
#     if i % a == 0:
#         m.append(i)
# print("a的公倍数为:" + str(m))
# for j in range(1, d + 1):
#     if j % b == 0:
#         n.append(j)
# print("b的公倍数为:" + str(n))
# for k in range(1, d + 1):
#     if k % c == 0:
#         o.append(k)
# print("c的公倍数为:" + str(o))  # 三个数组中存放了abc的公倍数
# f = []
# for i in m:
#     if (i in n):
#         if (i in o):
#             f.append(i)
#             f.sort()
#             print("a b c 的所有公倍数为:" + str(f[0]))


# 第二种求最小公倍数的方法
# 求三个数的最小公倍数，先设置一个number=1，循环判断number对abc取余，当余数同时为0，则跳出循环并输出number，否则继续循环number+=1
a = int(input("请输入a的值:"))
b = int(input("请输入b的值:"))
c = int(input("请输入c的值:"))
number = 1
while True:
    if number%a==0 and number%b==0 and number%c==0:
        print("abc的最小公倍数为:" + str(number))
        break
    else:
        number+=1

