
# 读入数字 并存放进列表
def In_put():
    '''
    也可以用这种写法
    empty_list=[] #定义一个空列表用以存放输入的num数字
    num = int(input('输入需要键入数字的个数:'))
    for i in range(num):
        num_a = int(input(f'请输入第{i+1}个数字:'))
        empty_list.append(num_a)
    return empty_list
    '''
    num_list = list(map(int, input("输入你需要的数字(以','逗号分隔):").split(',')))     #这种是简单的高阶函数写法

    return num_list


def get_max_min_avg(num):
    t = []
    for i in num:
        t.append(i)
    Max_num = max(t)
    Min_num = min(t)
    avg = sum(t)/len(t)
    print(f'\nMax_num={Max_num},Min_num={Min_num},agv={avg}')


if __name__ == '__main__':

    get_max_min_avg(In_put())



