# Import functions from our modules
from listen import take_command
from brain import process_command

# -----------------------------
# Main Program
# -----------------------------

print("🤖 Jarvis is now online!")

# Keep Jarvis running forever
while True:

    # Listen to the user
    command = take_command()

    # Show what Whisper understood
    print("\n🗣️ You said:")
    print(command)

    # Process the command
    if not process_command(command):
        break

print("🔴 Jarvis has stopped.")