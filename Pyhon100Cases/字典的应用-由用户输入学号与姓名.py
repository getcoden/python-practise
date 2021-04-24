'''
由用户输入学生学号与姓名，数据用字典存储，最终输出学生信息（按学号由小到大显示）。
用户输入信息，储存在字典里判断是否继续输入，继续填yes，输入其他则不继续继续输入时判断学号是否重复（名字不判断，名字存在多人重名情况），存在则不储存，重新输入，并储存在字典里对字典排序（字典转列表排序）
'''

# 1、由用户输入学生学号与姓名，数据用字典存储，最终输出学生信息（按学号由小到大显示）
# 创建字典
students = {}
# 用户输入
student = input("请输入学号：")
ID = input("请输入你的姓名:")
if not (student is None):
	students[student] = ID 
# 判断是否继续输入
judge = input("是否继续输入(请输入yes继续，输入其他则结束):")
while judge == "yes" or judge == "Yes":
	student = input("请输入学号：")
	ID = input("请输入你的姓名:")
# 判断学号是否重复,防止更改已输入的信息
	while student in students:
		if student in students:
			print('学号重复请重新输入你的信息')
			student = input("请输入学号：")
			ID = input("请输入你的姓名:")
		else:
			break
		# 加入字典
	students[student] = ID
	judge = input("是否继续输入(请输入yes或者no):")
# 排序
list1 = list(students.items())
list1.sort(key=lambda x: x[0], reverse=False)
print(dict(list1))