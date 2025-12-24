import webbrowser
from lib import music
from audio import speak

def handle(command):
    if command.startswith("play"):
        song = command.split(" ", 1)[1]
        if song in music:
            speak(f"Playing {song}")
            webbrowser.open(music[song])
        else:
            speak("Song not found")
        return True

    return False
