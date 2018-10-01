from gpiozero import Button
from signal import pause
from random import choice
import glob
import subprocess
import keyboard

def play_video():
    videos = []
    for file in glob.glob("/media/pi/Videos/*.mp4"):
        videos.append(file)
    print(videos)
    chosen = choice(videos)
    print(chosen)
    subprocess.Popen(['omxplayer',(chosen)])

def stop_video():
    keyboard.press_and_release('q')

def pause_video():
    keyboard.press_and_release('space')
    

randomiser = Button(2)
stop = Button(3)
pause_button = Button(4)
try:
    print("Press the GREEN button to start\nYELLOW to pause\nRED to stop")
    randomiser.when_pressed = play_video
    stop.when_pressed = stop_video
    pause_button.when_pressed = pause_video
    pause()
except KeyboardInterrupt:
    print("\nEXIT")

