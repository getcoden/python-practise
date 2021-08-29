from __future__ import unicode_literals
import youtube_dl

# 仅下载视频
times = int(input('输入要下载视频的数量:'))
for i in range(times):
    ydl_opts = {}
    ys_url = input(f'要下载{i+1}次的视频地址:')
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([ys_url])


# 仅下载视频的音频

ydl_opts = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
}

times = int(input('输入要下载音频的数量:'))
for i in range(times):
    y_url = input(f'要下载{i+1}次音频的视频的地址:')
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([y_url])
