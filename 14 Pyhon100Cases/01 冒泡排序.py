lis = [56, 12, 1, 8, 354, 10, 100, 34, 56, 7, 23, 456, 234, -58]


def sortport():
    for i in range(len(lis) - 1):
        for j in range(len(lis) - 1 - i):
            if lis[j] > lis[j + 1]:
                lis[j], lis[j + 1] = lis[j + 1], lis[j]
    return lis


if __name__ == '__main__':
    sortport()
    print(lis)
