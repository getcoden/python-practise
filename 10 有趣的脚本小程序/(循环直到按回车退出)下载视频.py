import youtube_dl
import os

os.chdir(r'D:\\音乐')  # 自定义设置下载文件保存的目录路径
while 1:
    ydl_opts = {}
    ysurl = input('要下载视频的地址:')
    if ysurl == '':
        print('已退出程序！')
        break
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        print('正在下载:')
        ydl.download([ysurl])

"""
import youtube_dl
import os 
# 设定
"""
os.chdir(r'设置下载文件保存的目录路径')  # 自定义设置下载文件保存的目录路径 或者用以下方法
"""
destPath = 'D:/Download/'    # 音频文件存放的目标字串
while 1:
    videoPage = input('要下载视频地址:')
    if videoPage=='':
        print('已退出程序！')
        break
    ydl_opts = {                              # 设定下载选项
                'outtmpl': destPath+'%(title)s.%(ext)s',
                'format': 'best',                
                }    
    print('正在下载:')
    ydl = youtube_dl.YoutubeDL(ydl_opts)
    ydl.download([videoPage])                 # 下载视频
    """
