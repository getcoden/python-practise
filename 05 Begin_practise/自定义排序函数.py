lst = [1, 3, 5, 9, 8, 6, 7, 2, 4]


def comp(a, b):
    return a < b


def sort(iterable, key=lambda a, b: a < b, reverse=True):

    ret = []
    for x in iterable:
        for i, y in enumerate(ret):
            flag = key(x, y) if reverse else key(y, x)
            if flag:
                ret.insert(i, x)
                break
        else:
            ret.append(x)

    return ret


print(sort(lst, reverse=False))
