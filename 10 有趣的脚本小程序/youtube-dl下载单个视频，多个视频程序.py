# 下载单个视频的
import youtube_dl

# 设定
destPath = 'D:/Download/'    # 音频文件存放的目标字串
videoPage = input('要下载视频地址:')

ydl_opts = {                              # 设定下载选项
    'outtmpl': destPath+'%(title)s.%(ext)s',
    'format': 'best',
}
ydl = youtube_dl.YoutubeDL(ydl_opts)
ydl.download([videoPage])                 # 下载视频


# 下载多个视频的
"""
   import youtube_dl

# 视频下载后的存放位置和视频链接

destPath = 'D:/Download/'     # 这个是要修改的

# 视频文件的播放列表地址，因为是多个所以才能以列表的形式下载

videoPage = 'https://www.youtube.com/playlist?list=PL8t-5XFBuHKWbPLFaUa6YpssAEi81ARN5'

# 钩子函数
def my_hook(d):
    if d['status'] == 'finished':
    # 如果视频下载完毕
        print('\n下载完毕后再输出视频信息：')
        for key, value in d.items():
            print("{}: {}".format(key, value))

ydl_opts = {
            'outtmpl': destPath+'%(title)s.%(ext)s',
            'format': 'best',
            'progress_hooks': [my_hook],           
             # 配置处理结果的钩子函数，函数传入的是一个视频信息的字典
            }
ydl = youtube_dl.YoutubeDL(ydl_opts)
ydl.download([videoPage])                     # 下载视频
    """
