from moviepy.editor import AudioFileClip

my_audio_clip = AudioFileClip(
    "D:\视频\️海来阿木【烟雨人间】️动态歌词.mp4")
my_audio_clip.write_audiofile("D:\视频\pyrj.mp3")  # .wav 格式文件较大
