import os


def tryMakeFile(filename):
    try:

        with open(filename) as _:

            return False

    except FileNotFoundError:

        with open(filename, mode='a') as _:

            return True


print(tryMakeFile('c:/Users/star/Desktop/1.txt'))
