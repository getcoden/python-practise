'''
Python 字典与集合的综合经典例题：输入学生的学号，姓名；或者输入学号，科目，成绩。以输入一行END为输入结束标志。最后格式化输出
'''
dictNumName = {}##存放第一种类型的输入：有学号，姓名。存放格式例如{"10":'张三','11':......}
dictNumScores = {}##存放第二种类型的输入：有学号，科目，成绩。
                  ##存放格式例如{'10':{'高数':80,'英语':85},'11'......}
courseName = set()##因为最后要在第一行输出表头，所以用一个集合，之后往里面添加时，就算有重复的科目也可以帮我们自动排重
while True:
    s = input()
    if s=='END':##以END 为结束标志
        break
    else:
        line = s.split(' ')##line是列表，里面有两个或者三个元素
        if len(line)==2:##line里面只有学号，姓名
            ##["10",'张三'],并且一个学号姓名只可能出现一次
            dictNumName[line[0]] = line[1] 
        else:##line里面是学号，一个选课，和其对应的成绩
            ##['10','高数',90],学号可能会多次出现，学生选修多门课
            if line[0] in dictNumScores:##这个line[0]学号之前已经出现过了
                d = dictNumScores.get(line[0])##所以dictNumScores在这个字典里已经有这个键，所以直接用d接一下返回的字典就可以了
                ##现在d = {xx:xx},有内容
                d[line[1]] = int(line[2])##
            else:
                d = {}##这个学号第一次出现，令d是一个新的空的字典
                dictNumScores[line[0]] = d##把line[0]作为键直接给dictNumScores，把d这个字典作为line[0]这个键的value。
                d[line[1]] = int(line[2])##给d赋新建一个键（科目名称）和值（该科目分数）
            courseName.add(line[1])##每次处理一个成绩，把科目名称加到集合里面
            
##输出
print('学号  姓名  ',end = '')
for item in courseName:
    print(item,end  = '  ')
print()
for key,value in dictNumScores.items():##{'19401050110':{'高数':80,'英语':85},'19401050111'......}
    
    ##按照key一个一个来，现在的key是'19401050110',value是{'高数':80,'英语':85}
    print(key+'  '+dictNumName[key]+'  '+str(value['高数'])+'  '+str(value['英语']))
    ##   
	