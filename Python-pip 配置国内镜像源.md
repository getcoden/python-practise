# Python-pip 配置国内镜像源

### 1.进入相应目录下 C 盘 ->Users / 用户 ->xxx-> 新建 pip 文件夹

### 2.进入 pip 文件夹 -> 新建 pip.ini 文件

### 3.进入 pip.ini 文件，并添加配置如下：（清华源）

>[global]
>index-url = https://pypi.tuna.tsinghua.edu.cn/simple
>[install]
>trusted-host = https://pypi.tuna.tsinghua.edu.cn  # trusted-host 此参数是为了避免麻烦，否则使用的时候可能会提示不受信任

### 4.修改完成后保存，启动 cmd，使用 "pip install xxx"(xxx 为你要下载的包名)，即可默认使用国内源下载。



----



# 如何将本地项目上传到 Github

1.点击 Clone or dowload 会出现一个地址，copy 这个地址备用。

2.接下来就到本地操作了，首先右键你的项目，如果你之前安装 git 成功的话，右键会出现两个新选项，分别为 Git Gui Here,Git Bash Here, 这里我们选择 Git Bash Here，进入如下界面，Test_Bluetooth 即为我的项目名。

3.接下来输入如下代码（关键步骤），把 github 上面的仓库克隆到本地**

git clone https://github.com/CKTim/BlueTooth.git（https://github.com/CKTim/BlueTooth.git 替换成你之前复制的地址）

4.这个步骤以后你的本地项目文件夹下面就会多出个文件夹，该文件夹名即为你 github 上面的项目名，如图我多出了个 Test 文件夹，我们把本地项目文件夹下的所有文件（除了新多出的那个文件夹不用），其余都复制到那个新多出的文件夹下，

5.接着继续输入命令 cd Test，进入 Test 文件夹

6.接下来依次输入以下代码即可完成其他剩余操作：

git add .    （注：别忘记后面的.，此操作是把 Test 文件夹下面的文件都添加进来）

git commit  -m  ''提交信息”  （注“提交信息” 里面换成你需要，如 “first commit”）

git push -u origin master  （注：此操作目的是把本地仓库 push 到 github 上面，此步骤需要你输入帐号和密码）
