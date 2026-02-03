import numpy as np
import pyaudio
from faster_whisper import WhisperModel

class SpeechToText:
    def __init__(self):
        self.model = WhisperModel(
            "small",
            compute_type="int8"
        )

        self.audio = pyaudio.PyAudio()

    def listen(self, seconds=5):
        stream = self.audio.open(
            format=pyaudio.paInt16,
            channels=1,
            rate=16000,
            input=True,
            frames_per_buffer=1024
        )

        frames = []
        for _ in range(0, int(16000 / 1024 * seconds)):
            frames.append(stream.read(1024))

        stream.stop_stream()
        stream.close()

        audio_data = np.frombuffer(b''.join(frames), np.int16).astype(np.float32) / 32768.0

        segments, _ = self.model.transcribe(audio_data)

        text = " ".join(segment.text for segment in segments)
        return text.strip()
