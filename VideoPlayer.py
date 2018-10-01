from gpiozero import Button
from signal import pause
from random import choice

import vlc

def play_video():
    videos = []
    for file in glob.glob("path to videos"):
        videos.append(file)
    to_play = choice(videos)
    print(to_play)
    player = vlc.MediaPlayer(to_play)
    player.play()

def stop_video():
    player.stop()

def pause_video():
    player.pause()
    

randomiser = Button(2)
stop = Button(3)
pause = Button(4)

randomiser.when_pressed = play_video
stop.when_pressed = stop_video
pause.when_pressed = pause_video

pause()
