# def collatz(num):
#     if num % 2 == 0:
#         return num // 2
#     elif num == 1:
#         return 1
#     elif num % 2 == 1:
#         return num * 3 + 1


# try:
#     a = int(input('Please input a num:\n'))
#     while True:
#         a = collatz(a)
#         print(a)
#         if a == 1:
#             break
# except ValueError:
#     print('Please input a right int num')

def collatz(number):
    n = number % 2
    if n == 0:
        number = number // 2
        print(number)
    elif n == 1:
        number = 3 * number + 1
        print(number)
        return number


print('Enter number:')
while True:
    try:
        a = int(input())
        if collatz(a) == 1:
            break
    except ValueError:
        print('invild int,please enter number:')
