import subprocess
from audio import speak

APP_MAP = {
    "safari": "Safari",
    "finder": "Finder",
    "terminal": "Terminal",
    "chrome": "Google Chrome",
    "vs code": "Visual Studio Code",
    "visual studio code": "Visual Studio Code",
}

def open_app(app_name):
    try:
        subprocess.Popen(["open", "-a", app_name])
        speak(f"Opening {app_name}")
    except Exception as e:
        print("App error:", e)
        speak("I could not open that application")

def set_volume(level):
    subprocess.Popen([
        "osascript", "-e",
        f"set volume output volume {level}"
    ])

def battery_status():
    try:
        output = subprocess.check_output(
            ["pmset", "-g", "batt"]
        ).decode()
        return output.split("\t")[1].split(";")[0]
    except:
        return None

def handle(command):
    command = command.lower().strip()

    if command.startswith("open "):
        app = command.replace("open ", "").strip()
        if app in APP_MAP:
            open_app(APP_MAP[app])
            return True

    if "increase volume" in command:
        set_volume(70)
        speak("Volume increased")
        return True

    if "decrease volume" in command:
        set_volume(30)
        speak("Volume decreased")
        return True

    if "mute volume" in command:
        set_volume(0)
        speak("Volume muted")
        return True

    if "battery" in command:
        percent = battery_status()
        if percent:
            speak(f"Battery is at {percent}")
        else:
            speak("Unable to read battery status")
        return True

    return False
