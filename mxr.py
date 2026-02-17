from datetime import datetime
from sys import exit
from time import sleep
import vlc


def play_song(source, volume):
    instance = vlc.Instance('--input-repeat=999')
    player = instance.media_player_new()
    player.audio_set_volume(volume)
    media = instance.media_new(source)
    player.set_media(media)
    player.play()
    sleep(2)
    raw_duration = int(media.get_duration())
    seconds = int((raw_duration / 1000) % 60)
    minutes = int(raw_duration / (60 * 1000) % 60)
    hours = int(raw_duration / (60 * 60 * 1000))
    print(f"  Playing: {source.split('/')[-1].split('.')[0]:>25}  -  Volume:", end=" ")
    print(f"{player.audio_get_volume()}  -  Duration:{hours:4d}:{minutes:02}:{seconds:02}\n")


# Audio data
tracks = [
    {"source": "file:///enter/folder/and/filename.mp3", "volume": 53},
    {"source": "file:///enter/folder/and/filename.mp3", "volume": 65},
    {"source": "file:///enter/folder/and/filename.mp3", "volume": 50},
]

# Display current time
print("\n  Start time:", datetime.now(), "\n")

# Play three songs to repeat 999 times each
play_song(tracks[0]["source"], tracks[0]["volume"])
play_song(tracks[1]["source"], tracks[1]["volume"])
play_song(tracks[2]["source"], tracks[2]["volume"])

# Display play time and close program with CTRL + C
count = 0
print("  'Ctrl+C' to exit\n")
try:
    while True:
        if count <= 60: 
            print(f"  Play time: {count} minutes", end="\r")
        else:
            hours = int(count / 60)
            minutes = int(count % 60)
            print(f"  Play time: {hours} hours and {minutes} minutes",end="\r")
        sleep(60)
        count += 1
except KeyboardInterrupt:
    print("  Goodbye !\n")
    exit(0)