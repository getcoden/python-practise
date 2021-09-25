# -*- coding:utf-8 -*-

from moviepy.editor import *

# 提取音频
video = VideoFileClip(
    r'D:\课件PPT\Reading at night Audio\真正毀掉一個人的是內耗行為！很多人都在做，卻不自知，聰明的你盡快戒掉【深夜讀書】.mp4')
audio = video.audio
audio.write_audiofile("D:/1jieya/11.mp3")

# 下面是批量处理：

"""
# -*- coding:utf-8 -*-
 
import os
 
from moviepy.video.io.VideoFileClip import VideoFileClip
 
print("路径示例(注意用反斜杠) D:/douyin/")
path_In = input('请输入提取路径:')
path_Out = input('请输入存储路径:')
 
os.chdir(path_In)  # 转到该目录下
get_dir = os.getcwd()  # os.getcwd()函数可以获取当前文件所在目录
lst = os.listdir(get_dir)  # os.listdir获取目录下所有文件 列表形式
for file in lst:
    if not os.path.isdir(file):  # 判断路径是否为目录
        if file.endswith('.mp4'):
            file_name = file.split('.mp4')[0],
            file_name = file_name[0]
            # print(file_name)
            pathIn = f"{path_In}{file}"
            pathOut = f"{path_Out}{file_name}.mp3"
            # 提取音频
            video = VideoFileClip(pathIn)
            audio = video.audio
            if audio:
                audio.write_audiofile(pathOut)
            else:
                print('audio为空...')
    """
# 输入输出路径 尽量不要用中文，有可能会报错 (注意路径用反斜杠): D:/demo/
