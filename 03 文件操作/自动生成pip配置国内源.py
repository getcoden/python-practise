"""
python建立pip.ini.py
2016年4月30日 03:35:11 codegay
"""
import os
ini = """[global]
index-url = https://pypi.mirrors.ustc.edu.cn/simple
[install]
trusted-host = https://pypi.mirrors.ustc.edu.cn  # trusted-host 此参数是为了避免麻烦，否则使用的时候可能会提示不受信任
"""
pippath = os.environ["USERPROFILE"]+"\\pip\\"
if not os.path.exists(pippath):
    os.mkdir(pippath)
with open(pippath+"pip.ini", "w+") as f:
    f.write(ini)
os.system('explorer.exe')
