import os
os.environ['IMAGEIO_FFMPEG_EXE'] = '/opt/homebrew/bin/ffmpeg'
import moviepy.editor as mp
import datetime

video1 = mp.VideoFileClip("video/gatto.mov")
final = video1.set_audio(mp.AudioFileClip("music/gatto2.wav"))

current_timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")

final.write_videofile(f"video/example_w_sound{current_timestamp}.mp4",
                      fps=30,
                      audio_codec="aac",
                      audio_bitrate="192k")