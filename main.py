from dotenv import load_dotenv
import speech_recognition as sr
from audio import verify_voice, listen_for_wake_word, create_recognizer, speak
from core import route

load_dotenv()

STOP_WORDS = ["stop", "sleep", "exit", "go to sleep"]

recognizer = create_recognizer()


def conversation_mode(recognizer):
    speak("Yes boss")

    while True:
        try:
            with sr.Microphone() as source:
                print("Listening for command...")
                audio = recognizer.listen(
                    source,
                    timeout=8,
                    phrase_time_limit=6
                )

            command = recognizer.recognize_google(audio).lower()
            print("You:", command)

            if any(stop in command for stop in STOP_WORDS):
                speak("Going back to sleep")
                break

            route(command)

        except sr.UnknownValueError:
            continue
        except sr.WaitTimeoutError:
            continue
        except sr.RequestError:
            speak("I need internet to understand commands")
            break
        except Exception as e:
            print("Conversation error:", e)
            break


if __name__ == "__main__":
    speak("Jarvis online")

    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source, duration=1)

    while True:
        print("Waiting for wake word (offline)...")

        listen_for_wake_word()
        speak("Voice verification")

        if verify_voice():
            conversation_mode(recognizer)
        else:
            speak("Access denied")

