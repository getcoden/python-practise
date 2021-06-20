import pprint
spam = ['cats', 'dogs', 'moose']
bacon = ['dogs', 'moose', 'cats']
# print(spam == bacon)

eggs = {'name': 'zophie', 'species': 'cat', 'age': '8'}
ham = {'species': 'cat', 'age': '8', 'name': 'zophie'}
# print(eggs == ham)

'''
birthdays = {'Alice': 'Apr 1', 'Bob': 'Dec 12', 'Carol': 'Mar 4'}
while True:
    print('Enter a name: (blank to quit)')
    name = input()
    if name == '':
        break
    if name in birthdays:
        print(birthdays[name] + ' is thd birthday of ' + name)
    else:
        print('I do not have birthday information for ' + name)
        print('What is their birthday')
        bday = input()
        birthdays[name] = bday
        print('Birthday database updated')
'''
message = 'It was a bright cold day in April, and the clocks were striking thirteen.'
count = {}
# for character in message:
#     count.setdefault(character, 0)
#     count[character] = count[character] + 1
# print(count)

# 改进版

# for character in message:
#     count.setdefault(character, 0)
#     count[character] = count[character] + 1
# pprint.pprint(count)

allGuests = {'Alice': {'apples': 5, 'pretzels': 12},
             'Bob': {'ham sandwiches': 3, 'apples': 2},
             'Carol': {'cups': 3, 'apple pies': 1}}


def totalBrought(guests, item):
    numBrought = 0
    for k, v in guests.items():
        numBrought = numBrought + v.get(item, 0)
    return numBrought


'''
print('Number of things being brought:')
print(' - Apples ' + str(totalBrought(allGuests, 'apples')))
print(' - Cups ' + str(totalBrought(allGuests, 'cups')))
print(' - Cakes ' + str(totalBrought(allGuests, 'cakes')))
print(' - Ham sandwiches ' + str(totalBrought(allGuests, 'ham sandwiches')))
print(' - Apples Pies ' + str(totalBrought(allGuests, 'apples pies')))
'''
# inventort.py

stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dangger': 1, 'arrow': 12}


def displayInventory(inventory):
    print('Inventory:')
    item_total = 0
    for k, v in inventory.items():
        print(str(v) + ' ' + k)
        item_total += v
    print('Total number of items: ' + str(item_total))


displayInventory(stuff)
