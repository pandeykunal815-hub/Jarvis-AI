# Import required libraries
import sounddevice as sd
from scipy.io.wavfile import write
from faster_whisper import WhisperModel


def take_command():
    """
    Record user's voice and convert it into text.

    Returns:
    str : The text recognized by Whisper.
    """

    # Recording settings
    duration = 5
    sample_rate = 44100
    output_file = "my_voice.wav"

    # Ask the user to speak
    print("🎤 Speak now...")

    # Record audio
    audio = sd.rec(
        int(duration * sample_rate),
        samplerate=sample_rate,
        channels=1,
        dtype="int16"
    )

    # Wait until recording is complete
    sd.wait()

    print("✅ Recording Complete!")

    # Save audio
    write(output_file, sample_rate, audio)

    print(f"💾 Audio saved as: {output_file}")

    # Load Whisper AI
    print("🧠 Loading Whisper Model...")

    model = WhisperModel("base", compute_type="int8")

    # Convert speech to text
    print("✍️ Converting speech to text...")

    segments, info = model.transcribe(
        output_file,
        beam_size=5,
        language="en",
        vad_filter=True
    )

    # Store recognized text
    user_text = ""

    for segment in segments:
        user_text += segment.text

    # Remove extra spaces
    user_text = user_text.strip()

    return user_text