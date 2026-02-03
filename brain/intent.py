import re

INTENTS = {
    "GET_TIME": [
        "time",
        "clock"
    ],
    "OPEN_YOUTUBE": [
        "youtube",
        "video"
    ],
    "OPEN_GOOGLE": [
        "google",
        "browser"
    ],
    "EXIT": [
        "exit",
        "quit",
        "stop",
        "bye"
    ]
}

def normalize(text: str) -> str:
    text = text.lower()
    text = re.sub(r"[^a-z0-9\s]", "", text)
    return text

def detect_intent(text: str) -> str:
    text = normalize(text)

    for intent, keywords in INTENTS.items():
        for keyword in keywords:
            if keyword in text:
                return intent

    return "CHAT"
