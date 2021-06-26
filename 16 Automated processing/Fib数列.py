import random
import os


def fibonacci(n):
    a = 0
    b = 1
    nums = []
    for _ in range(n):
        nums.append(a)
        a, b = b, a+b
    return nums


'''
while True:
    print('Enter a number:')
    shu = input()
    if shu == '':
        break

    print(fibonacci(int(shu)))
'''

fruit = ['apple', 'pear', 'pineapple', 'orange', 'banana']
# fruit = [x for x in fruit if x.startswith('a')]
# print(fruit)

# for i, x in enumerate(fruit):
#     print(i+1, x)

# 在字典中根据条件筛选数据


w = {key: random.randint(32, 40) for key in range(1, 8)}
print(w)

w1 = {key: val for key, val in w.items() if val > 35}
print(w1)
