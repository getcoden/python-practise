import math


def move(x, y, step, angle=0):
    nx = x+step*math.cos(angle)
    ny = y-step*math.sin(angle)
    return nx, ny


# a, b = move(4, 3, 5)
# print(a, b)

def enroll(name, gender, age=6, city='Beijing'):
    print('name:', name)
    print('gender:', gender)
    print('age:', age)
    print('city:', city)


# enroll('Sarah', 'F', city='tianwan')


def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum+n*n
    return sum


# print(calc(1, 2, 3))
# print(calc(1, 3, 5, 7))
# print(calc())

# nums = [1, 2, 3]
# print(calc(*nums))

# def fact(n):
    if n == 1:
        return 1
    return n*fact(n-1)


def fact(n):
    return fact_iter(n, 1)


def fact_iter(num, product):
    if num == 1:
        return product
    return fact_iter(num-1, num*product)


print(fact(5))

