import speech_recognition as sr
import subprocess

def create_recognizer():
    r = sr.Recognizer()
    r.energy_threshold = 200
    r.dynamic_energy_threshold = True
    r.dynamic_energy_adjustment_damping = 0.15
    r.dynamic_energy_ratio = 1.5
    r.pause_threshold = 0.8
    return r

def speak(text):
    subprocess.run(
        ["say", "-v", "Samantha", text]
    )
