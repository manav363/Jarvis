import webbrowser
from audio import speak

def handle(command):
    if "open google" in command:
        speak("Opening Google")
        webbrowser.open("https://google.com")
        return True

    if "open youtube" in command:
        speak("Opening YouTube")
        webbrowser.open("https://youtube.com")
        return True

    return False
