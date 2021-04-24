# a=eval(input("请输入学生姓名:"))
# b=eval(input("请输入学生成绩:"))
# c=dict(zip(a,b))
# print(c)

# key3=range(1,5)
# value3 = ['高上烽', '英大语', '折小磊', '线大代']
# dict_range = dict(zip(key3, value3))
# print(dict_range)

'''
循环输入若干学生信息（学号、姓名）保存到字典，并按学号排序。'''

a=int(input("请输入学生人数："))
num_list=[]
name_list=[]
d={}
for i in range(a):
    num=input("学号为：")
    name=input("姓名为：")
    print("\n")
    num_list.append(num)
    name_list.append(name)
    
d=dict(zip(num_list,name_list))
new_d=dict(sorted(d.items(),key=lambda x:x[0]))    
print(new_d)
