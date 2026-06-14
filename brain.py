
# Import required libraries
import os
import webbrowser
from datetime import datetime
from speak import speak


def process_command(command):
    """
    Process the user's command and
    decide how Jarvis should respond.

    Returns:
        True  -> Continue running
        False -> Stop Jarvis
    """

    # Convert text to lowercase
    command = command.lower().strip()

    # Possible ways Whisper may hear Jarvis
    wake_words = [
        "hello jarvis",
        "hello jarwish",
        "hello jar miss",
        "jarwish",
        "jar miss",
        "our wish",
        "no jar of wish"
    ]

    # Wake word detection
    if any(word in command for word in wake_words):

        speak("Hello Panda! I am Jarvis. How can I help you?")
        return True

    # Tell name
    elif "what is your name" in command:

        speak("My name is Jarvis.")
        return True

    # Creator
    elif "who created you" in command:

        speak("Panda is building me.")
        return True

    # Open YouTube
    elif "open youtube" in command:

        speak("Opening YouTube.")
        webbrowser.open("https://www.youtube.com")
        return True

    # Open Google
    elif "open google" in command:

        speak("Opening Google.")
        webbrowser.open("https://www.google.com")
        return True

    # Open GitHub
    elif "open github" in command:

        speak("Opening GitHub.")
        webbrowser.open("https://github.com")
        return True

    # Open ChatGPT
    elif "open chat g p t" in command or "open chatgpt" in command:

        speak("Opening Chat G P T.")
        webbrowser.open("https://chatgpt.com")
        return True

    # Open Calculator
    elif "open calculator" in command:

        speak("Opening Calculator.")
        os.system("calc")
        return True

    # Open Notepad
    elif "open notepad" in command:

        speak("Opening Notepad.")
        os.system("notepad")
        return True

    # Open VS Code
    elif "open visual studio code" in command or "open vs code" in command:

        speak("Opening Visual Studio Code.")
        os.system("code")
        return True

    # Tell current time
    elif "what time is it" in command or "tell me the time" in command:

        current_time = datetime.now().strftime("%I:%M %p")
        speak(f"Panda, the current time is {current_time}.")
        return True

    # Tell today's date
    elif "what is today's date" in command or "tell me the date" in command:

        current_date = datetime.now().strftime("%d %B %Y")
        speak(f"Panda, today is {current_date}.")
        return True

    # Exit Jarvis
    elif "goodbye jarvis" in command or "exit" in command:

        speak("Goodbye Panda. Have a nice day.")
        return False

    # Unknown command
    else:

        speak("Sorry Panda. I did not understand.")
        return True

