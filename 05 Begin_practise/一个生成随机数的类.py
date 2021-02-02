import random


class Randomgen():
    def show(self, n=10, a=1, b=100):
        lst = []
        for x in range(n):
            lst.append(random.randint(a, b))
        return lst


a = Randomgen()
print(a.show())
