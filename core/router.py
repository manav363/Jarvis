from skills import web, music, system, memory
from .ai import ask_ai
from audio import speak

SKILLS = [memory, system, web, music]

def route(command):
    for skill in SKILLS:
        if skill.handle(command):
            return

    response = ask_ai(command)
    print("Jarvis:", response)
    speak(response)
