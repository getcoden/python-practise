from moviepy.editor import AudioFileClip

my_audio_clip = AudioFileClip(
    "D:\视频\S1E01- Betty's Tomato Truck goes through the car wash.mp4")
my_audio_clip.write_audiofile("D:\视频\py02.mp3") # .wav 格式文件较大
