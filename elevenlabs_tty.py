import os
import uuid

from dotenv import load_dotenv
from elevenlabs import VoiceSettings
from elevenlabs.client import ElevenLabs

# Load environment variables from .env file
load_dotenv()

# Retrieve the API key from the .env file
api_key = os.getenv("ELEVENLABS_API_KEY")

# Pass the API key to the client
client = ElevenLabs(api_key=api_key)


def text_to_speech_file(text: str) -> str:
    """
    Converts text to speech and saves the output as an MP3 file.

    This function uses a specific client for text-to-speech conversion. It configures
    various parameters for the voice output and saves the resulting audio stream to an
    MP3 file with a unique name.

    Args:
        text (str): The text content to convert to speech.

    Returns:
        str: The file path where the audio file has been saved.
    """
    # Calling the text_to_speech conversion API with detailed parameters
    response = client.text_to_speech.convert(
        voice_id="Gqe8GJJLg3haJkTwYj2L",  # Santa Claus voice
        optimize_streaming_latency="0",
        output_format="mp3_22050_32",
        text=text,
        model_id="eleven_turbo_v2", 
        # model_id="eleven_multilingual_v2",
        voice_settings=VoiceSettings(
            stability=0.0,
            similarity_boost=1.0,
            style=0.0,
            use_speaker_boost=True,
        ),
    )

    # Generating a unique file name for the output MP3 file
    save_file_path = f"eleven.mp3"
    # Writing the audio stream to the file

    with open(save_file_path, "wb") as f:
        for chunk in response:
            if chunk:
                f.write(chunk)

    print(f"A new audio file was saved successfully at {save_file_path}")

    # Return the path of the saved audio file
    return save_file_path

# text_to_speech_file("This is a test")

text_to_speech_file("""
Once upon a time, in the vast night sky, there lived a little star named Luma. She wasn't as big or bright as the other stars, and she often felt unnoticed. But she had a dream—to shine her light on something truly special.

One chilly December night, Luma noticed a commotion among the stars. "What’s happening?" she asked.

“The Great Star has a task for us!” said a glowing comet. “A very special child is being born on Earth, and one of us must guide the way to him.”

Luma's heart leapt. Could this be her chance? She twinkled as brightly as she could and floated to the Great Star.

“I want to help!” she said, her voice tiny but full of hope.
""")