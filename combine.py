from pydub import AudioSegment
from pydub.playback import play

# Load your audio files
speech = AudioSegment.from_file("eleven.mp3")  # Replace with your Eleven Labs audio file
background = AudioSegment.from_file("sounds/jingle_bells.mp3")  # Replace with your background music file

# Adjust volumes if necessary
speech = speech + 5  # Increase volume of speech
background = background - 15  # Lower volume of background music

# Adjust the background music to match the length of the speech
if len(background) > len(speech):
    # Trim the background music
    background = background[:len(speech)]
else:
    # Loop the background music
    loops_needed = len(speech) // len(background) + 1
    background = (background * loops_needed)[:len(speech)]

# Overlay the audio files
combined = background.overlay(speech)

# Play the combined audio
play(combined)

# Save the combined audio to a file
combined.export("combined_audio.mp3", format="mp3")