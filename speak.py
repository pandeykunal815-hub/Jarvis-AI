

import pyttsx3

# Initialize speech engine
engine = pyttsx3.init()

# Set speaking speed
engine.setProperty("rate", 170)

# Select voice
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[1].id)


def speak(text):
    """
    Convert text into speech.
    """

    print(f"🤖 Jarvis: {text}")

    engine.say(text)
    engine.runAndWait()
