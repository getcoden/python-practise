students = {}


def showmenu():
    msg = '学生管理系统\
    \n1、增加\
    \n2、删除\
    \n3、更新\
    \n4、查询\
    \n5、显示所有\
    \n6、退出'
    print(msg)


def addstu():
    name = input('学生姓名:')
    stuID = input('学号:')
    while True:
        if stuID in students.keys():
            stuID = input('已存在，请重新输入:')
        else:
            break
    students[stuID] = name
    print('\n添加成功')


def deletestu():
    stuID = input('输入要删除的学号：')
    while True:
        if stuID not in students.keys():
            stuID = input('不存在，请重新输入:')
        else:
            break
    del (students[stuID])
    print('\n删除成功')


def updatestu():
    stuID = input('输入要更新学号:')
    while True:
        if stuID not in students.keys():
            stuID = input('不存在，重新输入:')
        else:
            break
    name = input('修改学生的姓名:')
    students[stuID] = name
    print('\n修改成功')


def selectstu():
    stuID = input('输入要查询学号:')
    name = students.get(stuID, None)
    if name:
        print('学号对应的姓名:', name)
    else:
        print('学号不存在')


def selectall():
    print('系统中有以下学生:\n')
    for stuID in students:
        print(stuID, students[stuID])
    print('查询结束')


while True:
    showmenu()
    choice = int(input('请选择操作:'))
    if choice == 1:
        addstu()
    elif choice == 2:
        deletestu()
    elif choice == 3:
        updatestu()
    elif choice == 4:
        selectstu()
    elif choice == 5:
        selectall()
    elif choice == 6:
        break
    else:
        print('输入无效，重新输入')
