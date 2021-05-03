'''
a = int(input('输入学生人数:'))
num_list = []
name_list = []
d = {}
for i in range(a):
    num = input('学号为:')
    name = input('姓名为:')
    print('\n')
    num_list.append(num)
    name_list.append(name)
d = dict(zip(name_list, num_list))
new_d = dict(sorted(d.items(), key=lambda x: x[0]))
print(new_d)
'''

# students = []
# count = 3
# for i in range(count):
#     name = input(f'请输入第{i+1}个学生的姓名:')
#     age = input(f'请输入第{i+1}个学生的年龄:')
#     gender = input(f'请输入第{i+1}个学生的性别:')
#     score = input(f'请输入第{i+1}个学生的成绩:')
#     stu_list = [name, age, gender, score]
#     students.append(stu_list)
# for stu in students:
#     for v in stu:
#         print(v, end=' ')
#     print()

# 简单登陆
'''
_name = '123'
_password = '456'
name = input('name:')
password = input('password:')
if _name == name and _password == password:
    print('welcome user {name} login......'.format(name=name))
    print('---------------------')
else:
    print('Invalid password')
'''

# 猜大小程序

number = 20
for i in range(1, 10, 2):
    guess_number = int(input('guess number:'))
    if guess_number == number:
        print('yes,you got it!')
    elif guess_number > number:
        print('think bigger!')
    print('loop', i)
