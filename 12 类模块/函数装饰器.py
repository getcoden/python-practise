# def foo():
# 	print('foo')
# def bar(func):
# 	func()
# 	print('i am bar')
# bar(foo)

# print_msg是外围函数
# def print_msg():
#     msg = "I'm closure"

#     # printer是嵌套函数
#     def printer():
#         print(msg)

#     return printer

# closure = print_msg()
# print(closure)
# closure()



import functools
# import logging
# from collections.abc import Iterable
def log(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print('call %s():' % func.__name__)
        print('args = {}'.format(*args))
        return func(*args, **kwargs)

    return wrapper

@log
def test(p):
	print(test.__name__ + 'param:' + p)
test("I'm a param")

# def use_logging(func):
# 	def wrapper():
# 		logging.warn('%s is running' % func.__name__)
# 		return func()
# 	return wrapper

# @use_logging
# def foo():
# 	print("I'm foo")

# # foo = use_logging(foo)
# foo()

# def use_logging(level):
#     def decorator(func):
#         def wrapper(*args, **kwargs):
#             if level == "warn":
#                 logging.warn("%s is running" % func.__name__)
#             elif level == "info":
#                 logging.info("%s is running" % func.__name__)
#             return func(*args)
#         return wrapper

#     return decorator

# @use_logging(level="warn")
# def foo(name='foo'):
#     print("i am %s" % name)

# foo()

# class Foo(object):
#     def __init__(self, func):
#         self._func = func

#     def __call__(self):
#         print ('class decorator runing')
#         self._func()
#         print ('class decorator ending')

# @Foo
# def bar():
#     print ('bar')

# bar()

# import functools

# def log_with_param(text):
#     def decorator(func):
#         @functools.wraps(func)
#         def wrapper(*args, **kwargs):
#             print('call %s():' % func.__name__)
#             print('args = {}'.format(*args))
#             print('log_param = {}'.format(text))
#             return func(*args, **kwargs)

#         return wrapper

#     return decorator
    
# @log_with_param("param")
# def test_with_param(p):
#     print(test_with_param.__name__)

# # 传入装饰器的参数，并接收返回的decorator函数
# decorator = log_with_param("param")
# # 传入test_with_param函数
# wrapper = decorator(test_with_param)
# # 调用装饰器函数
# wrapper("I'm a param")


