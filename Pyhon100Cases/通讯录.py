#初始状态时，联系人a对应的地址为A，联系人b对应的地址为B，联系人c,d对应的地址分别为C,D
addressList={'a':'A','b':'B','c':'C','d':'D'}
print("XX的通讯录".center(30,('*')))
print("addressList=",addressList)
while 1:
    i=input("请选择需要的操作：【1】添加；【2】修改；【3】删除；【0】退出\n")
    if int(i)==1:
        name=input('请输入新增姓名：')
        add=input("住址：")
        addressList[name]=add
        print('已添加！')
    elif int(i)==2:
        name=input('请输入需要修改的人的姓名：')
        print(name,'的原地址为：',addressList[name])
        add=input('请输入新地址：')
        addressList[name]=add
        print('已修改')
    elif int(i)==3:
        name=input('请输入需要删除的联系人的姓名：')
        print('需要删除',name,'的信息吗？')
        l=input('确认输入YES\n')
        if l=='YES':
            del addressList[name]
            print('删除成功！')
        else:
            print('删除失败')
    elif int(i)==0:
        break
print('addressList=',addressList)
print("已退出".center(30,('*')))