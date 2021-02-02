# 代码免费开源使用
# 请检查代码完整性

try:
    from random import choice
    import sys

    # 设出词库
    ku_a = 'q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'a', 's', 'd', 'f',\
           'g', 'h', 'j', 'k', 'l', 'z', 'x', 'c', 'v', 'b', 'n', 'm'
    ku_A = 'Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P', 'A', 'S', \
           'D', 'F', 'G', 'H', 'J', 'K', 'L', 'Z', 'X', 'C', 'V', 'B', 'N', 'M'
    ku_0 = '0', '1', '2', '3', '4', '5', '6', '7', '8', '9'
    ku_ = '~', '@', '#', '%', '^', '&', '*', '(', ')', '-', '=', '+'
    # 了解需求
    input('请回答以下问题 是为1 否  点击回车继续')
    ku_a_ = input('你是否加入小写字母：')
    ku_A_ = input('你是否加入大写字母：')
    ku_0_ = input('你是否需要数字组合：')
    ku_s = input('你是否需要特殊符号')
    # 判断需求
    aaa, AAA, k000, sss = '有', '有', '有', '有'
    if ku_a_ != '1':
        ku_a = ()

        aaa = '无'
    if ku_A_ != '1':
        ku_A = ()
        AAA = '无'
    if ku_0_ != '1':
        ku_0 = ()
        k000 = '无'
    if ku_s != '1':
        ku_ = ()
        sss = '无'
    if (ku_a + ku_A + ku_0 + ku_) == ():
        print('没有选择')
        input('软件退出')
        sys.exit()
    # 询问次数
    b = input('你需要多少位数密码')
    e = input('你需要生成多少次')
    f = int(e)
    a = int(b)
    if a > 100 or f > 10000:
        print('位数最多为100位,且不能超过生成10000次')

        sys.exit()
    if a < 0 or f < 0:
        print('无法生成负数')
        sys.exit()
    d = ''
    cun = ''
    cuns = ('密码位数：'+b+'\n'
            '生成数量：'+e+'\n'
            '复杂系数：'+'\n'
            '    '+'小写：'+aaa+'\n'
            '    '+'大写：'+AAA+'\n'
            '    '+'数字：'+k000 + '\n'
            '    '+'特殊符号：'+sss+'\n')
    print(cuns)

    print('正在执行')
    # 开始执行
    for b in range(f):
        for b in range(a):
            c = (choice(ku_a + ku_A + ku_0 + ku_))
            d += c

        cun += (d)
        cun += ('\n')
        d = ''
    print(cun)
    ss = input('是否保存 是1 或 否0')
    if ss == '否' or ss == '0':
        input('回车退出软件')
    if ss == '是' or ss == '1':
        lujings = input('请复制路径到这里:')
        wenjianmings = input('输入文件名字:')
        lujing = lujings + '/' + wenjianmings + '.txt'
        with open(lujing, 'w') as f:
            cuns += cun

            f.write(cuns)
        print('已经尝试在', lujings, '下创建', wenjianmings, '.txt')
except:
    print('软件被你玩坏啦\n你输入的请求无法被正常理解')
    input('')
