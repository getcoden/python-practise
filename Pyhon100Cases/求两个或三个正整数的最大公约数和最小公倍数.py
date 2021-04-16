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
