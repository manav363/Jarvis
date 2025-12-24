from resemblyzer import VoiceEncoder, preprocess_wav
import sounddevice as sd
import numpy as np

SAMPLE_RATE = 16000
DURATION = 3
THRESHOLD = 0.65

encoder = VoiceEncoder()
stored_embedding = np.load("data/my_voice_embedding.npy")

def verify_voice():
    audio = sd.rec(
        int(DURATION * SAMPLE_RATE),
        samplerate=SAMPLE_RATE,
        channels=1,
        dtype="float32"
    )
    sd.wait()

    wav = preprocess_wav(audio.flatten(), SAMPLE_RATE)
    new_embedding = encoder.embed_utterance(wav)

    similarity = np.dot(stored_embedding, new_embedding)

    print(f"[VOICE-ID] Similarity score: {similarity:.3f}")

    return similarity > THRESHOLD
