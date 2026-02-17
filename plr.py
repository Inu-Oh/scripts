from datetime import datetime
from os import path
from sys import exit
from time import sleep
import vlc


def main():
    # Get song data
    while True:
        src = input("Source file:/// ...: ")
        try: 
            file_ext = src.split(".")[-1]
        except:
            print(f'Invalid input')
            continue
        if file_ext not in ["mp3", "ogg", "wav", "flac", "aac"]:
            print(f'Wrong file type. Must be mp3, ogg", wav, flac or aac.')
            continue
        elif path.isfile(src):
            break
        print(f'Source file not found at "{src}"')
    vol = -1
    while vol < 0 or vol > 100:
        vol = int(input("Volume 0-100: "))

    # Display current time and play song
    print("\n  Start time:", datetime.now(), "\n")
    real_volume, hrs, mins, secs = play_song(src, vol)
    print(f"  Playing: {src.split('/')[-1].split('.')[0]:>25}  -  Volume:", end=" ")
    print(f"{real_volume}  -  Duration:{hrs:4d}:{mins:02}:{secs:02}\n")

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
                print(f"  Play time: {hours} hours and {minutes} minutes", end="\r")
            sleep(60)
            count += 1
    except KeyboardInterrupt:
        print("\n\n  Goodbye !\n")
        exit(0)

def play_song(source, volume):
    """Play a song on repeat given source and volume from prompt."""
    instance = vlc.Instance('--input-repeat=999') # change repeats if needed
    player = instance.media_player_new()
    player.audio_set_volume(volume)
    media = instance.media_new("file:///path/to/file/folder/" + source)
    player.set_media(media)
    player.play()
    sleep(2)
    raw_duration = int(media.get_duration())
    seconds = round((raw_duration / 1000) % 60)
    minutes = round(raw_duration / (60 * 1000) % 60)
    hours = round(raw_duration / (60 * 60 * 1000))
    real_volume = player.audio_get_volume()
    return real_volume, hours, minutes, seconds


if __name__ == "__main__":
    main()
