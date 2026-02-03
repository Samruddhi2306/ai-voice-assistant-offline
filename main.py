from brain.llm import LocalLLM
from audio.stt import SpeechToText
from brain.intent import detect_intent
from tools.time_tool import get_current_time
from tools.browser_tool import open_youtube, open_google
from tools.system_tool import exit_program
from speech.tts import TextToSpeech

# Initialize components
stt = SpeechToText()
tts = TextToSpeech()
llm = LocalLLM()

print("🎤 Speak now...")
text = stt.listen(seconds=7)

if not text:
    tts.speak("I didn't catch that. Please repeat.")
    exit()

print("📝 Raw text:", text)

intent = detect_intent(text)
print("🧠 Detected intent:", intent)

if intent == "GET_TIME":
    response = f"The time is {get_current_time()}"
    print("⏰", response)
    tts.speak(response)

elif intent == "OPEN_YOUTUBE":
    response = "Opening YouTube"
    print("📺", response)
    tts.speak(response)
    open_youtube()

elif intent == "OPEN_GOOGLE":
    response = "Opening Google"
    print("🌐", response)
    tts.speak(response)
    open_google()

elif intent == "EXIT":
    tts.speak("Goodbye")
    exit_program()

elif intent == "CHAT":
    response = llm.generate(text)
    print("🤖", response)
    tts.speak(response)

else:
    tts.speak("I am not sure how to help with that.")
