# class Person:
# 	def __init__(self):
# 		self.name = '张三'
# 		self.age = 21
		

# 	def walk(self):
# 		print('走路')
# 	def run(self):
# 		print('跑步')


# p = Person()  # 发现属性可以自动执行
# print(p.name)
# print(p.age)



#为了重复调用，用变量赋值属性
# class Person:
# 	def __init__(self,name,age):
# 		self.name = name
# 		self.age = age
		

# 	def walk(self):
# 		print('走路')
# 	def run(self):
# 		print('跑步')


# p = Person('张三', 21)  #实现动态赋值
# p1 = Person('李四', 22)  #实现动态赋值
# p2 = Person('王五', 34)  #实现动态赋值
# print(p.name,p.age)
# print(p1.name,p.age)
# print(p2.name, p.age)

# 类方法
class Dog:
	def __init__(self, name):
		self.name = name
	def walk(self):
		print(f'{self.name}狗:会跳高')

dog1 = Dog('哈真一')
dog1.age = 10
print(dog1.name, dog1.age)
dog1.walk()

dog2 = Dog('金毛')
dog2.age = 22
print(dog2.name, dog2.age)
dog2.walk()