# spam = r'this is Alice\'s cat'
# print(spam)
# 字符串方法 upper(),lower(),isupper()和 islower()

# spam = 'Hello World!'
# spam = spam.lower()  # 必须在该字符串上调用lower()或upper(),才能用这个新字符
# 串赋给保存原来字符串的变量，这就是为什么必须使用spam=spam.lower()了
# print(spam)

'''
while True:
    print('How are you?')
    feeling = input()
    if feeling == '':
        break
    elif feeling.lower() == 'great':
        print('I fell great too.')
    else:
        print('I hope the rest of your day is good.')
'''
import pyperclip
spam = 'Hello world!'
# print(spam.islower())
# print('Hello'.upper().lower().upper().islower())

# print('hello'.isalpha())
# print('hello123'.isalpha())
# print('hello123'.isalnum())
# print('hello'.isalnum())
# print('123'.isdigit())
# print(' '.isdecimal())

# while True:
#     print('Enter your age:')
#     age = input()
#     if age.isdecimal():
#         break
#     print('Please enter a number for your age.')
# while True:
#     print('Select a new password(letters and numbers only):')
#     password = input()
#     if password.isalnum():
#         break
#     print('Passowords can only have letters and numbers')

# print("Hello world!".startswith('Hello'))
# print("Hello world!".endswith('!'))
# print("abc123".startswith('abc'))
# print("abc123".endswith('123'))
# print("Hello world!".endswith('Hello world'))

# print(','.join(['cats', 'rats', 'bats']))
# print(' '.join(['My', 'name', 'is', 'Simon']))
# print('ABC '.join(['My', 'name', 'is', 'Simon']))

# print('My name is Simon'.split())

# print('Hello'.rjust(10, '='))
# print('Hello'.ljust(10, '-'))
# print('Hello'.center(10, '-'))

'''
def printPicnic(itemsDict, leftWidth, rightWidth):
    print('PICNIC ITEMS'.center(leftWidth + rightWidth, '-'))
    for k, v in itemsDict.items():
        print(k.ljust(leftWidth, '.') + str(v).rjust(rightWidth))


printItems = {'sandwiches': 4, 'apples': 12, 'cups': 4, 'cookies': 8000}
printPicnic(printItems, 12, 5)
printPicnic(printItems, 20, 6)
'''
# spam = '        Hello world!  gsfdg '
# print(spam.strip())
# print(spam.lstrip())
# print(spam.rstrip())

# pyperclip.copy('Hello world!')
# print(pyperclip.paste())

# text = pyperclip.paste()
# lines = text.split('\n')
# for i in range(len(lines)):
#     lines[i] = '* ' + lines[i]
# text = '\n'.join(lines)
# pyperclip.copy(text)
# print('Remember, remember, the fifth of November.'.split())
# print('-'.join('There can be only one.'.split()))

"""下面是代码正文"""
tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]


def printTable(tableData):
    colWidths = [0] * len(tableData)
    for i in range(len(colWidths)):
        colWidths[i] = len(sorted(tableData[i], key=(lambda x: len(x)))[-1])

    for x in range(len(tableData)):
        for y in range(len(tableData)):
            print(tableData[y][x].rjust(colWidths[y]), end=' ')
        print('')


printTable(tableData)
