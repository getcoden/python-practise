
#(1)

import os
os.getcwd()
path = os.getcwd()
os.listdir(path)



#(2)

import os
result = []
def get_all(cwd):
    get_dir = os.listdir(cwd)
    for i in get_dir:
        sub_dir = os.path.join(cwd,i)
        if os.path.isdir(sub_dir):
            get_all(sub_dir)
        else:
            result.append(i)
if __name__ == "__main__":
    get_all(r'D:\Wowode\jupyterlab\test')
    print(result)
    print('共计有{}个文件'.format(len(result)))
            