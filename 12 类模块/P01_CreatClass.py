# 关键字class + 类名:   类名采用驼峰命名法，如 class OnePerson:

class Person:
	def walk(self):
		print('走路')
	def run(self):
		print('跑步')

#实例化类
p = Person()
p.walk()
p.run()

#可以创建多类实例
p1 = Person()
p2 = Person()

#创建了不调用不会输出
p1.run()

p.name = '张三'
p.age = 23
print(p.name)
print(p.age)