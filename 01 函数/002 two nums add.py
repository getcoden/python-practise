def fun(a,b):
    c=a+b
    print(c)

while 1:
    num1=int(input('Eenter the first number:'))
    num2=int(input('Eenter the second number:'))
    fun(num1,num2)
    is_continue=input('是否再来一次(yes/no?)')
    if is_continue!='y':
        break
    else:
        continue
        


def da():   
    def sum_2_num(num1,num2):
        '''动态计算两个数相加'''
        result = num1+num2
        return result

    num=int(input('请输入你要计算的次数:'))
    tol=1
    while tol<=num:
        num1=int(input('Enter first number:'))
        num2=int(input('Enter second number:'))
        rs=sum_2_num(num1,num2)
        print('{}'.format(rs))
        tol+=1


da() 