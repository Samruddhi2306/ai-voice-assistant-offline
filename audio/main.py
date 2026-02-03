from audio.stt import SpeechToText

stt = SpeechToText()

print("🎤 Speak now...")
text = stt.listen(seconds=5)

print("📝 You said:", text)