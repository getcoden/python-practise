def flist(args):
    print('��������:',len(args))
    for i,k in enumerate(args):
        print("��{}������{}:".format(i,k))
    print(args)
b=[]
a = input('>>>:').split()
for j in a:
    b.append(int(j))
flist(b)