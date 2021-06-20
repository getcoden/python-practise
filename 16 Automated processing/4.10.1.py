def list2str(alist):
    print(alist)
    a = alist.pop()
    a = 'and' + a
    alist.append(a)
    b = ','.join(alist)
    return b  # print改成return 就可以返回结果


a = ['cat', 'dog', 'cow']
print(list2str(a))
