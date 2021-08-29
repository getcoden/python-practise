from __future__ import unicode_literals
import youtube_dl
import os

os.chdir(r"D:\课件PPT\Reading at night Audio")

ydl_opts = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
}

while 1:
    y_url = input('要下载音频的视频的地址:')
    if y_url == '':
        print('已退出程序！')
        break
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        print('正在下载:')
        ydl.download([y_url])
