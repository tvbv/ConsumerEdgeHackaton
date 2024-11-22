from pydub import AudioSegment
from pydub.playback import play

# Load your audio files
speech = AudioSegment.from_file("eleven.mp3")  # Replace with your Eleven Labs audio file
background = AudioSegment.from_file("sounds/jingle_bells.mp3")  # Replace with your background music file

# Adjust volumes if necessary
# speech = speech + 5  # Increase volume of speech
background = background - 7  # Lower volume of background music

# Overlay the audio files
combined = background.overlay(speech)

# Play the combined audio
play(combined)

# Optional: Save the combined audio to a file
combined.export("combined_audio.mp3", format="mp3")
