from dotenv import load_dotenv
import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary
from openai import OpenAI
import os

load_dotenv()

recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    try:
        engine.say(text)
        engine.runAndWait()
    except Exception as e:
        print("Speech error:", e)

def aiProcess(command):
    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

    response = client.responses.create(
        model="gpt-4o-mini",
        input=f"You are Jarvis. Keep answers short.\nUser: {command}"
    )
    return response.output_text

def processCommand(c):
    c = c.lower()

    if "open google" in c:
        speak("Opening Google")
        webbrowser.open("https://google.com")

    elif "open youtube" in c:
        speak("Opening YouTube")
        webbrowser.open("https://youtube.com")

    elif "open facebook" in c:
        speak("Opening Facebook")
        webbrowser.open("https://facebook.com")

    elif c.startswith("play"):
        song = c.split(" ")[1]
        if song in musicLibrary.music:
            speak(f"Playing {song}")
            webbrowser.open(musicLibrary.music[song])
        else:
            speak("Song not found")

    else:
        output = aiProcess(c)
        print("Jarvis:", output)
        speak(output)

if __name__ == "__main__":
    speak("Initializing Jarvis...")

    while True:
        try:
            with sr.Microphone() as source:
                print("Listening for wake word...")
                audio = recognizer.listen(source, timeout=2, phrase_time_limit=1)

            word = recognizer.recognize_google(audio).lower()

            if word == "jarvis":
                speak("Yes boss")

                with sr.Microphone() as source:
                    print("Jarvis Active...")
                    audio = recognizer.listen(source)

                command = recognizer.recognize_google(audio)
                print("You:", command)

                # Speak AFTER mic closes
                processCommand(command)

        except Exception as e:
            print("Error:", e)
