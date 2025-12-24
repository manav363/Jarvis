from storage import remember, recall, forget, summary
from audio import speak

def normalize_key(text):
    text = text.lower().strip()
    for word in ["my", "the", "a", "an", "please"]:
        text = text.replace(f"{word} ", "")
    return text.strip()

def handle(command):
    command = command.lower()

    if command.startswith("remember"):
        data = command.replace("remember", "").strip()

        for filler in ["that", "please"]:
            if data.startswith(filler + " "):
                data = data.replace(filler + " ", "", 1)

        if " is " in data:
            key, value = data.split(" is ", 1)
        elif " as " in data:
            key, value = data.split(" as ", 1)
        else:
            speak("Please say remember something is something")
            return True

        key = normalize_key(key)
        remember("profile", key, value.strip())
        speak("I have remembered that")
        return True

    if command.startswith("what is my"):
        key = normalize_key(command.replace("what is my", ""))
        value = recall(key)

        if value:
            speak(f"Your {key} is {value}")
        else:
            speak("I do not have that information yet")
        return True

    if command.startswith("forget"):
        key = normalize_key(command.replace("forget", ""))
        if forget(key):
            speak("I have forgotten that")
        else:
            speak("I could not find that information")
        return True

    if "what do you remember about me" in command:
        items = summary()
        if items:
            speak("I remember the following about you")
            for item in items:
                speak(item)
        else:
            speak("I do not remember anything yet")
        return True

    return False
