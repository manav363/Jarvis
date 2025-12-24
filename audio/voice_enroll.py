from resemblyzer import VoiceEncoder, preprocess_wav
import sounddevice as sd
import soundfile as sf
import numpy as np

SAMPLE_RATE = 16000
DURATION = 6

print("Speak clearly for 6 seconds...")

audio = sd.rec(
    int(DURATION * SAMPLE_RATE),
    samplerate=SAMPLE_RATE,
    channels=1,
    dtype="float32"
)
sd.wait()

sf.write("data/my_voice.wav", audio, SAMPLE_RATE)

wav = preprocess_wav("data/my_voice.wav")
encoder = VoiceEncoder()
embedding = encoder.embed_utterance(wav)

np.save("data/my_voice_embedding.npy", embedding)

print("Voice profile saved ✅")
