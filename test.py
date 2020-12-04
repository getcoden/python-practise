def flist(args):
    print('参数个数:',len(args))
    for i,k in enumerate(args):
        print("第{}个参数{}:".format(i,k))
    print(args)
b=[]
a = input('>>>:').split()
for j in a:
    b.append(int(j))
flist(b)